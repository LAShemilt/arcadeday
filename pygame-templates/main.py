import pygame as pg
from background import Background

def main():
        """this function is called when the program starts.
        it initializes everything it needs, then runs in
        a loop until the function returns."""
        # Initialize Everything
        pg.init()
        screen = Background()
        screen.display()
        
        clock = pg.time.Clock()
        going = True
        while going:
            clock.tick(60)

            # Handle Input Events
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    going = False
                elif event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                    going = False

            
            
        pg.quit()

if __name__=='__main__':
    main()

