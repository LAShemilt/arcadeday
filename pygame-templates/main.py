import pygame as pg
from background import Background
from sprites import FranklinImp

def main():
        """this function is called when the program starts.
        it initializes everything it needs, then runs in
        a loop until the function returns."""
        # Initialize Everything
        pg.init()
        screen = Background(color = (123,210,10))#image_path="data/lab.png")
        screen.create_background()
        screen.display()

        imp = FranklinImp("data/sprite.png")
        allsprites = pg.sprite.Group((imp))
        clock = pg.time.Clock()
        going = True
        while going:
            clock.tick(60)

            # Handle Input Events
            for event in pg.event.get():
                # Quit the program
                if event.type == pg.QUIT:
                    going = False
                elif event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                    going = False

                # Move the sprite
                elif event.type == pg.KEYDOWN and event.key == pg.K_DOWN:
                     imp.update()
                # Interactions
            allsprites.update()

           
            allsprites.draw(screen.screen)

        pg.quit()

if __name__=='__main__':
    main()

