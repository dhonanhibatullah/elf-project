import pygame as pg



class ElfTrajStudio:



    def __init__(self) -> None:
        
        # Members
        self.is_running = False



    def init(self, trajectory_name:str, track_filename:str) -> None:

        # Running ok
        self.is_running = True

        
        # Parameters
        WINDOW_TITLE    = f'ELF Project Trajectory Studio  |  {trajectory_name}'
        PYGAME_WIDTH    = 720
        PYGAME_HEIGHT   = 720


        # Initiate pygame
        pg.init()
        pg.display.set_caption('ELF Project Trajectory Studio  |  Image loading...')
        self.screen = pg.display.set_mode((PYGAME_WIDTH, PYGAME_HEIGHT))
        self.clock  = pg.time.Clock()


        # Transform the image to desirable size
        DESIRED_WIDTH   = 720
        DESIRED_HEIGHT  = 720

        original_img    = pg.image.load(track_filename)
        width, height   = original_img.get_size()
        
        if width > height:
            scale = DESIRED_WIDTH/width
        else:
            scale = DESIRED_HEIGHT/height
        

        # Result
        self.track_img              = pg.transform.smoothscale_by(original_img, scale)
        self.track_img_rect         = self.track_img.get_rect()
        self.track_img_rect.center  = (PYGAME_WIDTH//2, PYGAME_HEIGHT//2)
        self.traj_name              = trajectory_name
        pg.display.set_caption(WINDOW_TITLE)



    def isOk(self) -> bool:
        return self.is_running



    def loop(self) -> None:
        
        # Terminate if close
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.destroy()
                return


        # Fill screen
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.track_img, self.track_img_rect)


        # Update
        pg.display.update()
        self.clock.tick(60)



    def destroy(self) -> None:
        self.is_running = False
        pg.quit()