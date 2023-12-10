import tkinter as tk
import pygame as pg



class ElfTrajStudio:



    def __init__(self) -> None:

        # Parameters
        self.TOOLWIN_TITLE   = f'Elf Project Trajectory Studio  |  Tools Window'
        self.TOOLWIN_WIDTH   = 480
        self.TOOLWIN_HEIGHT  = 720
        self.PYGAME_TITLE    = lambda name: f'ELF Project Trajectory Studio  |  {name}'
        self.PYGAME_WIDTH    = 720
        self.PYGAME_HEIGHT   = 720
        self.PYGAME_CENTER_X = self.PYGAME_WIDTH//2
        self.PYGAME_CENTER_Y = self.PYGAME_HEIGHT//2

        
        # Members
        self.is_running         = False
        self.track_img_scale    = 1.0
        self.mouser_pressed     = False
        self.mousel_pressed     = False
        self.start_pos_x        = 0
        self.start_pos_y        = 0
        self.diff_pos_x         = 0
        self.diff_pos_y         = 0
        self.disp_x             = 0
        self.disp_y             = 0



    def init(self, trajectory_name:str, track_filename:str) -> None:

        # Running ok
        self.is_running = True


        # Initiate tkinter for tools window
        self.root = tk.Tk()
        self.root.title(self.TOOLWIN_TITLE)
        self.root.geometry(f'{self.TOOLWIN_WIDTH}x{self.TOOLWIN_HEIGHT}+{(self.root.winfo_screenwidth()-self.TOOLWIN_WIDTH)//2}+{(self.root.winfo_screenheight()-self.TOOLWIN_HEIGHT)//2}')
        self.root.resizable(False, False)
        self.root.protocol('WM_DELETE_WINDOW', self.destroy)


        # Initiate pygame
        pg.init()
        pg.display.set_caption('ELF Project Trajectory Studio  |  Image loading...')
        self.screen = pg.display.set_mode((self.PYGAME_WIDTH, self.PYGAME_HEIGHT))
        self.clock  = pg.time.Clock()


        # Transform the image to desirable size
        DESIRED_WIDTH   = self.PYGAME_WIDTH
        DESIRED_HEIGHT  = self.PYGAME_HEIGHT

        original_img    = pg.image.load(track_filename)
        width, height   = original_img.get_size()
        
        if width > height:
            scale = DESIRED_WIDTH/width
        else:
            scale = DESIRED_HEIGHT/height
        

        # Resulting image
        self.base_track_img         = pg.transform.smoothscale_by(original_img, scale)
        self.track_img              = self.base_track_img
        self.track_img_rect         = self.track_img.get_rect()
        self.track_img_rect.center  = (self.PYGAME_CENTER_X, self.PYGAME_CENTER_Y)
        self.traj_name              = trajectory_name


        # Change window title
        pg.display.set_caption(self.PYGAME_TITLE(trajectory_name))



    def isOk(self) -> bool:
        return self.is_running



    def loop(self) -> None:
        
        # Check for events
        for event in pg.event.get():
            
            # Quit the trajectory studio
            if event.type == pg.QUIT:
                self.destroy()
                return
            
            # Mousewheel for zoom in and out
            if event.type == pg.MOUSEWHEEL:

                if event.y > 0 and self.track_img_scale < 10.0:
                    self.track_img_scale += 0.5
                
                elif event.y < 0 and self.track_img_scale > 1.0:
                    self.track_img_scale -= 0.5

            # Click
            if event.type == pg.MOUSEBUTTONDOWN:
                
                # Left down to start navigates
                if event.button == 1:
                    self.mousel_pressed = True
                    self.start_pos_x, self.start_pos_y = pg.mouse.get_pos()

                # Right down for placing trajectory points
                elif event.button == 3:
                    self.mouser_pressed = True

            if event.type == pg.MOUSEBUTTONUP:
                
                # Save the last position
                if event.button == 1:
                    self.mousel_pressed = False
                    self.disp_x -= self.diff_pos_x
                    self.disp_y -= self.diff_pos_y
                
                elif event.button == 3:
                    self.mouser_pressed = False


        # Determine the track image displacement from mouse movement
        current_x, current_y = pg.mouse.get_pos()

        if self.mousel_pressed:
            self.diff_pos_x = self.start_pos_x - current_x
            self.diff_pos_y = self.start_pos_y - current_y
            
            # The center displacement
            self.track_img_rect.center = (self.PYGAME_CENTER_X + self.disp_x - self.diff_pos_x, self.PYGAME_CENTER_Y + self.disp_y - self.diff_pos_y)


        # Render the screen display
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.track_img, self.track_img_rect)


        # Update
        pg.display.update()
        self.root.update()
        self.clock.tick(60)



    def destroy(self) -> None:
        self.is_running = False
        self.root.destroy()
        pg.quit()