import os
import tkinter as tk
from src.gui.page.elf_main_page import ElfMainPage
from src.gui.page.elf_trjstd_page import ElfTrjstdPage
from src.gui.page.elf_trjwrt_page import ElfTrjwrtPage
from src.gui.page.elf_settings_page import ElfSettingsPage
from src.gui.page.elf_trjstdcrt_page import ElfTrjstdcrtPage
from src.gui.elf_gui_events import *



class ElfGui:



    def __init__(self) -> None:
        
        # Parameters
        WINDOW_TITLE    = 'ELF Project by Dhonan'
        WINDOW_WIDTH    = 480
        WINDOW_HEIGHT   = 640


        # Members
        self.status         = True
        self.current_page   = MAIN_PAGE

        self.trjstd_event   = False
        self.traj_name      = ''
        self.track_filename = ''


        # Initiate tkinter window
        self.root = tk.Tk()
        self.root.title(WINDOW_TITLE)
        self.root.geometry(f'{WINDOW_WIDTH}x{WINDOW_HEIGHT}+{(self.root.winfo_screenwidth()-WINDOW_WIDTH)//2}+{(self.root.winfo_screenheight()-WINDOW_HEIGHT)//2}')
        self.root.resizable(False, False)
        self.root.protocol('WM_DELETE_WINDOW', self.destroy)


        # Initiate pages
        self.page   = {
            MAIN_PAGE           : ElfMainPage(self.root),
            TRJSTD_START_PAGE   : ElfTrjstdPage(self.root),
            TRJWRT_PAGE         : ElfTrjwrtPage(self.root),
            SETTINGS_PAGE       : ElfSettingsPage(self.root),
            TRJSTDCRT_PAGE      : ElfTrjstdcrtPage(self.root)
        }
        self.page[MAIN_PAGE].draw()



    def isEventAvailable(self) -> bool:
        retval              = self.trjstd_event
        self.trjstd_event   = False
        return retval



    def getTrjstdEvent(self) -> tuple:
        return (True, self.traj_name, self.track_filename)



    def isOk(self) -> bool:
        return self.status



    def loop(self) -> None:

        # Update app state
        self.root.update()


        # Check the event from current page
        page_event = self.page[self.current_page].getPageEvent()
        if page_event == NULL_EVENT: return
        

        # MAIN PAGE EVENTS
        if self.current_page == MAIN_PAGE:
            

            if page_event == MAIN_PAGE_TRJSTD:

                # Hide the old page and show the new one
                self.page[self.current_page].hide()
                self.current_page = TRJSTD_START_PAGE
                self.page[self.current_page].draw()


            elif page_event == MAIN_PAGE_TRJWRT:

                # Hide the old page and show the new one
                self.page[self.current_page].hide()
                self.current_page = TRJWRT_PAGE
                self.page[self.current_page].draw()


            elif page_event == MAIN_PAGE_SETTINGS:

                # Hide the old page and show the new one
                self.page[self.current_page].hide()
                self.current_page = SETTINGS_PAGE
                self.page[self.current_page].draw()


            elif page_event == MAIN_PAGE_APP_DESTROY:
                self.destroy()


        elif self.current_page == TRJSTD_START_PAGE:


            if page_event == TRJSTD_START_PAGE_CRTTRJ:

                # Hide the old page and show the new one
                self.page[self.current_page].hide()
                self.current_page = TRJSTDCRT_PAGE
                self.page[self.current_page].draw()


            elif page_event == TRJSTD_START_PAGE_EDTTRJ:
                pass


            elif page_event == TRJSTD_START_PAGE_BACK:

                # Hide the old page and show the new one
                self.page[self.current_page].hide()
                self.current_page = MAIN_PAGE
                self.page[self.current_page].draw()


        elif self.current_page == TRJWRT_PAGE:


            if page_event == TRJWRT_PAGE_WRITE:
                pass


            elif page_event == TRJWRT_PAGE_BACK:

                # Hide the old page and show the new one
                self.page[self.current_page].hide()
                self.current_page = MAIN_PAGE
                self.page[self.current_page].draw()


        elif self.current_page == SETTINGS_PAGE:


            if page_event == SETTINGS_PAGE_BACK:

                # Hide the old page and show the new one
                self.page[self.current_page].hide()
                self.current_page = MAIN_PAGE
                self.page[self.current_page].draw()


        elif self.current_page == TRJSTDCRT_PAGE:


            if page_event == TRJSTDCRT_PAGE_OK:
                
                # Get trajectory name and track filename from user
                (valid, self.traj_name, self.track_filename) = self.page[TRJSTDCRT_PAGE].getInput()

                # If valid, back to main menu with disabled trjstd button
                if valid:
                    self.trjstd_event = True
                    self.page[self.current_page].hide()
                    self.current_page = MAIN_PAGE
                    self.page[self.current_page].draw()
                    self.page[self.current_page].button_trjstd.config(state='disabled')


            if page_event == TRJSTDCRT_PAGE_BACK:

                # Hide the old page and show the new one
                self.page[self.current_page].hide()
                self.current_page = TRJSTD_START_PAGE
                self.page[self.current_page].draw()



    def destroy(self) -> None:
        self.status = False