import tkinter as tk
from src.gui.elf_gui_events import *
from src.lib.elf_serial import ElfSerial



class ElfTrjwrtPage:



    def __init__(self, root) -> None:

        # Parameters
        self.BG_COLOR    = '#091413'
        self.FG_COLOR    = '#E4F0EE'


        # Members
        self.event          = NULL_EVENT
        self.elf_serial     = ElfSerial()
        self.selected_port  = tk.StringVar()
        self.selected_plan  = ''

        
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


        # Label: Select serial port
        self.label1 = tk.Label(
            master  = self.frame_master,
            bg      = self.BG_COLOR,
            fg      = self.FG_COLOR,
            text    = 'Select serial port:',
            font    = ('Calibri Light', 16)
        )


        # Label: Select trajectory to write
        self.label2 = tk.Label(
            master  = self.frame_master,
            bg      = self.BG_COLOR,
            fg      = self.FG_COLOR,
            text    = 'Select trajectory to write:',
            font    = ('Calibri Light', 16)
        )
        

        # Button: Start write
        self.button_write = tk.Button(
            master  = self.frame_master,
            bg      = self.BG_COLOR,
            fg      = self.FG_COLOR,
            relief  = tk.GROOVE,
            text    = 'Start write!',
            font    = ('Calibri Light', 16),
            command = lambda : self.onButtonClick(event=TRJWRT_PAGE_WRITE)
        )
        self.button_write.bind('<Enter>', lambda e: self.onButtonEnter(e=e, obj=self.button_write))
        self.button_write.bind('<Leave>', lambda e: self.onButtonLeave(e=e, obj=self.button_write))


        # Button: Back to main menu
        self.button_back = tk.Button(
            master  = self.frame_master,
            bg      = self.BG_COLOR,
            fg      = self.FG_COLOR,
            relief  = tk.GROOVE,
            text    = 'Back to main menu',
            font    = ('Calibri Light', 16),
            command = lambda : self.onButtonClick(event=TRJWRT_PAGE_BACK)
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


        # Draw button: Select serial port
        self.label1.place(
            anchor      = tk.N,
            relx        = 0.5,
            rely        = 0.25
        )


        # Draw button: Select trajectory to write
        self.label2.place(
            anchor      = tk.N,
            relx        = 0.5,
            rely        = 0.4
        )


        # Draw button: Start write
        self.button_write.place(
            anchor      = tk.N,
            relx        = 0.5,
            rely        = 0.72,
            relwidth    = 0.8,
            relheight   = 0.1
        )


        # Draw button: Back to main menu
        self.button_back.place(
            anchor      = tk.N,
            relx        = 0.5,
            rely        = 0.85,
            relwidth    = 0.8,
            relheight   = 0.1
        )


        # Draw option menu for serial
        if self.elf_serial.findPort():
            self.selected_port.set('Select port')
        else: 
            self.selected_port.set('No port available')

        self.option_port = tk.OptionMenu(
            self.frame_master,
            self.selected_port,
            *self.elf_serial.port_list
        )
        self.option_port.place(
            anchor      = tk.N,
            relx        = 0.5,
            rely        = 0.31,
            relwidth    = 0.8,
            relheight   = 0.06
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