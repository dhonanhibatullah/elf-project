import threading
import time
from src.gui.elf_gui_events import *
from src.gui.elf_gui import ElfGui
from src.gui.elf_trjstd import ElfTrajStudio



# Parameters
FPS_TICK = 1./60.



# Globs and mutexes
elf_trjstd_run              = False
elf_trjstd_traj_name        = ''
elf_trjstd_track_filename   = ''
elf_trjstd_close            = False
elf_trjstd_reenable         = False
elf_trjstd_mutex            = threading.Lock()
elf_trjstd_smutex           = threading.Lock()



# GUI task
def elf_gui_task():

    # Get the globals
    global elf_trjstd_run
    global elf_trjstd_traj_name
    global elf_trjstd_track_filename
    global elf_trjstd_close
    global elf_trjstd_reenable
    global elf_trjstd_mutex
    global elf_trjstd_smutex


    # Local variables
    trjstd_run = False


    # Declare GUI instance
    elf_gui = ElfGui()


    # Loop
    while elf_gui.isOk():

        # Loop the GUI
        elf_gui.loop()


        # Fetch any incoming event from the GUI
        if elf_gui.isEventAvailable():
            with elf_trjstd_mutex:
                (elf_trjstd_run, elf_trjstd_traj_name, elf_trjstd_track_filename) = elf_gui.getTrjstdEvent()
                trjstd_run = True


        # Re-enable Trajectory studio button
        if trjstd_run:
            with elf_trjstd_smutex:
                if elf_trjstd_reenable:
                    elf_gui.page[MAIN_PAGE].button_trjstd.config(state='normal')
                    elf_trjstd_reenable = False
                    trjstd_run          = False


    # Close everything
    elf_gui.root.destroy()
    with elf_trjstd_mutex: elf_trjstd_close = True



# Trajectory studio task
def elf_trjstd_task():

    # Get the globals
    global elf_trjstd_run
    global elf_trjstd_traj_name
    global elf_trjstd_track_filename
    global elf_trjstd_close
    global elf_trjstd_reenable
    global elf_trjstd_mutex
    global elf_trjstd_smutex


    # Local variable
    elf_traj_studio = ElfTrajStudio()
    trjstd_run      = False

    
    # Loop
    while True:

        if elf_traj_studio.isOk():
            elf_traj_studio.loop()
            

        # Update running state
        with elf_trjstd_mutex:

            # Open the trajectory studio and stop the latch
            if elf_trjstd_run:
                elf_traj_studio.init(elf_trjstd_traj_name, elf_trjstd_track_filename)
                elf_trjstd_run  = False
                trjstd_run      = True

            if trjstd_run and not elf_traj_studio.isOk():
                with elf_trjstd_smutex: elf_trjstd_reenable = True
                trjstd_run = False

            if elf_trjstd_close:
                break



# Define threads
elf_gui_thread      = threading.Thread(target=elf_gui_task)
elf_trjstd_thread   = threading.Thread(target=elf_trjstd_task)