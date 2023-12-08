import os
import tkinter as tk
from tkinter import filedialog
from src.gui.elf_gui_events import *



class ElfTrjstdcrtPage:



    def __init__(self, root) -> None:

        # Parameters
        self.BG_COLOR   = '#091413'
        self.BG_COLOR1  = '#000501'   
        self.FG_COLOR   = '#E4F0EE'


        # Members
        self.event      = NULL_EVENT
        self.filename   = ''

        
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


        # Label: Insert trajectory name
        self.label1 = tk.Label(
            master  = self.frame_master,
            bg      = self.BG_COLOR,
            fg      = self.FG_COLOR,
            text    = 'Trajectory name:',
            font    = ('Calibri Light', 16)
        )

        
        # Entry: Trajectory name
        self.entry_trjname = tk.Entry(
            master              = self.frame_master,
            bg                  = self.BG_COLOR1,
            fg                  = self.FG_COLOR,
            insertbackground    = self.FG_COLOR,
            relief              = tk.GROOVE,
            font                = ('Calibri Light', 14),
            justify             = 'center'
        )


        # Label: Select track layout
        self.label2 = tk.Label(
            master  = self.frame_master,
            bg      = self.BG_COLOR,
            fg      = self.FG_COLOR,
            text    = 'Select track layout (.png):',
            font    = ('Calibri Light', 16)
        )


        # Button: Find track file
        self.button_findfile = tk.Button(
            master  = self.frame_master,
            bg      = self.BG_COLOR,
            fg      = self.FG_COLOR,
            relief  = tk.GROOVE,
            text    = 'Search file',
            font    = ('Calibri Light', 16),
            command = lambda : self.openFileExplorer()
        )
        self.button_findfile.bind('<Enter>', lambda e: self.onButtonEnter(e=e, obj=self.button_findfile))
        self.button_findfile.bind('<Leave>', lambda e: self.onButtonLeave(e=e, obj=self.button_findfile))
        

        # Button: Proceed to trjstd
        self.button_next = tk.Button(
            master  = self.frame_master,
            bg      = self.BG_COLOR,
            fg      = self.FG_COLOR,
            relief  = tk.GROOVE,
            text    = 'Proceed to trajectory studio',
            font    = ('Calibri Light', 16),
            command = lambda : self.onButtonClick(event=TRJSTDCRT_PAGE_OK)
        )
        self.button_next.bind('<Enter>', lambda e: self.onButtonEnter(e=e, obj=self.button_next))
        self.button_next.bind('<Leave>', lambda e: self.onButtonLeave(e=e, obj=self.button_next))


        # Button: Back to previous menu
        self.button_back = tk.Button(
            master  = self.frame_master,
            bg      = self.BG_COLOR,
            fg      = self.FG_COLOR,
            relief  = tk.GROOVE,
            text    = 'Back',
            font    = ('Calibri Light', 16),
            command = lambda : self.onButtonClick(event=TRJSTDCRT_PAGE_BACK)
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


        # Draw label: Insert trajectory name
        self.label1.place(
            anchor      = tk.N,
            relx        = 0.5,
            rely        = 0.28,
        )


        # Draw entry: Trajectory name
        self.entry_trjname.delete(0, tk.END)
        self.entry_trjname.place(
            anchor      = tk.N,
            relx        = 0.5,
            rely        = 0.34,
            relwidth    = 0.8,
            relheight   = 0.06
        )


        # Draw label: Select track
        self.label2.place(
            anchor      = tk.N,
            relx        = 0.5,
            rely        = 0.43
        )

        
        # Draw button: Find track file
        self.filename = ''
        self.button_findfile.config(text='Search file')
        self.button_findfile.place(
            anchor      = tk.N,
            relx        = 0.5,
            rely        = 0.49,
            relwidth    = 0.8,
            relheight   = 0.1
        )


        # Draw button: Proceed to trjstd
        self.button_next.place(
            anchor      = tk.N,
            relx        = 0.5,
            rely        = 0.72,
            relwidth    = 0.8,
            relheight   = 0.1
        )


        # Draw button: Back to previous menu
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



    def openFileExplorer(self) -> None:
        
        # Open file dialog
        self.filename = filedialog.askopenfilename(
            initialdir  = '/',
            title       = 'Select track file',
            filetypes   = [("PNG files", "*.png"), ("All files", "*.*")]
        )

        # Display the file name on button
        dirs        = self.filename.split('/')
        filename    = dirs[-1]
        self.button_findfile.config(
            text    = filename,
            justify = 'left'
        )



    def getPageEvent(self) -> int:
        event       = self.event
        self.event  = NULL_EVENT
        return event
    


    def getInput(self) -> tuple:

        # Get user input
        trajname = str(self.entry_trjname.get())
        filename = str(self.filename)

        # Check whether the input is valid
        if (len(trajname) != 0) and os.path.exists(filename):
            return (True, trajname, filename)
        else:
            self.button_next.config(text='Invalid input, try again!')
            return (False, '', '')