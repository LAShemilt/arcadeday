import pygame as pg

def main():
        """this function is called when the program starts.
        it initializes everything it needs, then runs in
        a loop until the function returns."""
        # Initialize Everything
        pg.init()
        screen = pg.display.set_mode((1280, 480), pg.SCALED)
        pg.display.set_caption("AI Away Day")
        pg.mouse.set_visible(False)
        clock = pg.time.Clock()

        # Create The Background
        background = pg.Surface(screen.get_size())
        background = background.convert()
        background.fill((170, 238, 187))

        # Put Text On The Background, Centered
        if pg.font:
            font = pg.font.Font(None, 64)
            text = font.render("RFI-Arcade", True, (10, 10, 10))
            textpos = text.get_rect(centerx=background.get_width() / 2, y=10)
            background.blit(text, textpos)

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

