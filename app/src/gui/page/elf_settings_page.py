import tkinter as tk
from src.gui.elf_gui_events import *



class ElfSettingsPage:



    def __init__(self, root) -> None:

        # Parameters
        self.BG_COLOR    = '#091413'
        self.FG_COLOR    = '#E4F0EE'


        # Members
        self.event  = NULL_EVENT

        
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


        # Button: Back to main menu
        self.button_back = tk.Button(
            master  = self.frame_master,
            bg      = self.BG_COLOR,
            fg      = self.FG_COLOR,
            relief  = tk.GROOVE,
            text    = 'Back to main menu',
            font    = ('Calibri Light', 16),
            command = lambda : self.onButtonClick(event=SETTINGS_PAGE_BACK)
        )
        self.button_back.bind('<Enter>', lambda e: self.onButtonEnter(e=e, obj=self.button_back))
        self.button_back.bind('<Leave>', lambda e: self.onButtonLeave(e=e, obj=self.button_back))



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


        # Draw button: Back to main menu
        self.button_back.place(
            anchor      = tk.N,
            relx        = 0.5,
            rely        = 0.85,
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