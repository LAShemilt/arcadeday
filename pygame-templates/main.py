import pygame as pg
from arena import Arena
from sprites import FranklinImp, TestTube, SpriteConfig

def main():
        """this function is called when the program starts.
        it initializes everything it needs, then runs in
        a loop until the function returns."""
        # Initialize Game
        pg.init()

         # Initialize Arena
        arena = Arena(config="configs/arena_config.yml")
        arena.create_background()
        arena.display()
        pg.display.flip()

        # Initialize Sprites
        imp = FranklinImp("configs/sprite_config.yml")
        tube = TestTube("configs/testtube_config.yml", arena.background)
        allsprites = pg.sprite.Group(imp, tube) # You can create groups of sprites for updates
        tubes = pg.sprite.Group(tube)

        #Intilize clock sets the frame update rate in the game
        clock = pg.time.Clock()

        # The Game Loop
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
                elif event.type == pg.KEYDOWN and event.key == pg.K_LEFT:
                     imp.update(-1)
                elif event.type == pg.KEYDOWN and event.key == pg.K_RIGHT:
                     imp.update(1)
                
                # Sprite Interactions
                if pg.sprite.spritecollide(imp, tubes, 1):
                     tube.catch()
                     imp.jump()
                     tube.update()
                     game_over= SpriteConfig("configs/game_over_config.yml")
                     allsprites.add(game_over)

            # Update the characters with current state
            tube.update()
            arena.screen.blit(arena.background, (0, 0))
            allsprites.draw(arena.screen)
            
            pg.display.flip()     

        pg.quit()

if __name__=='__main__':
    main()

