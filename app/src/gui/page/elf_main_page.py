import tkinter as tk
from src.gui.elf_gui_events import *



class ElfMainPage:



    def __init__(self, root) -> None:

        # Parameters
        self.BG_COLOR    = '#091413'
        self.FG_COLOR    = '#E4F0EE'


        # Members
        self.event = NULL_EVENT

        
        # Initiate page
        self.root = root
        self.frame_master = tk.Frame(
            master  = self.root,
            bg      = self.BG_COLOR
        )


        # Title
        self.label_title = tk.Label(
            master  = self.frame_master,
            bg      = self.BG_COLOR,
            fg      = self.FG_COLOR,
            text    = 'ELF Project',
            font    = ('Calibri Light', 40, 'bold')
        )


        # Subtitle
        self.label_subtitle = tk.Label(
            master  = self.frame_master,
            bg      = self.BG_COLOR,
            fg      = self.FG_COLOR,
            text    = 'by Dhonan   |   v1.0',
            font    = ('Calibri Light', 16)
        )


        # Button: Trajectory studio
        self.button_trjstd = tk.Button(
            master  = self.frame_master,
            bg      = self.BG_COLOR,
            fg      = self.FG_COLOR,
            relief  = tk.GROOVE,
            text    = 'Open trajectory studio',
            font    = ('Calibri Light', 16),
            command = lambda : self.onButtonClick(event=MAIN_PAGE_TRJSTD)
        )
        self.button_trjstd.bind('<Enter>', lambda e: self.onButtonEnter(e=e, obj=self.button_trjstd))
        self.button_trjstd.bind('<Leave>', lambda e: self.onButtonLeave(e=e, obj=self.button_trjstd))


        # Button: Write trajectory
        self.button_trjwrt = tk.Button(
            master  = self.frame_master,
            bg      = self.BG_COLOR,
            fg      = self.FG_COLOR,
            relief  = tk.GROOVE,
            text    = 'Write trajectory to elf',
            font    = ('Calibri Light', 16),
            command = lambda : self.onButtonClick(event=MAIN_PAGE_TRJWRT)
        )
        self.button_trjwrt.bind('<Enter>', lambda e: self.onButtonEnter(e=e, obj=self.button_trjwrt))
        self.button_trjwrt.bind('<Leave>', lambda e: self.onButtonLeave(e=e, obj=self.button_trjwrt))


        # Button: Settings
        self.button_settings = tk.Button(
            master  = self.frame_master,
            bg      = self.BG_COLOR,
            fg      = self.FG_COLOR,
            relief  = tk.GROOVE,
            text    = 'Settings',
            font    = ('Calibri Light', 16),
            command = lambda : self.onButtonClick(event=MAIN_PAGE_SETTINGS)
        )
        self.button_settings.bind('<Enter>', lambda e: self.onButtonEnter(e=e, obj=self.button_settings))
        self.button_settings.bind('<Leave>', lambda e: self.onButtonLeave(e=e, obj=self.button_settings))


        # Button: Exit
        self.button_exit = tk.Button(
            master  = self.frame_master,
            bg      = self.BG_COLOR,
            fg      = self.FG_COLOR,
            relief  = tk.GROOVE,
            text    = 'Exit ELF Project',
            font    = ('Calibri Light', 16),
            command = lambda : self.onButtonClick(event=MAIN_PAGE_APP_DESTROY)
        )
        self.button_exit.bind('<Enter>', lambda e: self.onButtonEnter(e=e, obj=self.button_exit))
        self.button_exit.bind('<Leave>', lambda e: self.onButtonLeave(e=e, obj=self.button_exit))



    def draw(self) -> None:

        # Draw master frame
        self.frame_master.place(
            anchor      = tk.NW,
            relx        = 0.0,
            rely        = 0.0,
            relwidth    = 1.0,
            relheight   = 1.0
        )


        # Draw title
        self.label_title.place(
            anchor      = tk.N,
            relx        = 0.5,
            rely        = 0.04
        )


        # Draw subtitle
        self.label_subtitle.place(
            anchor      = tk.N,
            relx        = 0.5,
            rely        = 0.145
        )


        # Draw button: Trajectory studio
        self.button_trjstd.place(
            anchor      = tk.N,
            relx        = 0.5,
            rely        = 0.3,
            relwidth    = 0.8,
            relheight   = 0.1
        )


        # Draw button: Write trajectory
        self.button_trjwrt.place(
            anchor      = tk.N,
            relx        = 0.5,
            rely        = 0.45,
            relwidth    = 0.8,
            relheight   = 0.1
        )


        # Draw button: Settings
        self.button_settings.place(
            anchor      = tk.N,
            relx        = 0.5,
            rely        = 0.6,
            relwidth    = 0.8,
            relheight   = 0.1
        )


        # Draw button: Exit
        self.button_exit.place(
            anchor      = tk.N,
            relx        = 0.5,
            rely        = 0.75,
            relwidth    = 0.8,
            relheight   = 0.1
        )



    def hide(self) -> None:
        self.frame_master.place_forget()


    
    def onButtonEnter(self, e, obj) -> None:
        obj.config(
            bg  = '#AFCCC9',
            fg  = self.BG_COLOR
        )


    
    def onButtonLeave(self, e, obj) -> None:
        obj.config(
            bg  = self.BG_COLOR,
            fg  = self.FG_COLOR
        )



    def onButtonClick(self, event) -> None:
        self.event = event



    def getPageEvent(self) -> int:
        event       = self.event
        self.event  = NULL_EVENT
        return event