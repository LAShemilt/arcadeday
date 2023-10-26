import pygame as pg
from pathlib import Path

class Background:
    def __init__(self):
        self.image = Path('data/background.png')
        self.display_width = 1280
        self.display_height = 480
        self.display_caption ="AI Away Day"
        self.mouse_visible = False
        self.color = (124,32,124)
    
    def display(self):
        self.screen = pg.display.set_mode((self.display_width, self.display_height), pg.SCALED)
        pg.display.set_caption(self.display_caption)

        # Create The Background
        self.background = pg.Surface(self.screen.get_size())
        self.background.convert()
        self.background.fill(self.color)
        self.screen.blit(self.background, (0, 0))
        pg.display.flip()

    def add_text(self):

        # Put Text On The Background, Centered
        if pg.font:
            font = pg.font.Font(None, 64)
            text = font.render("RFI-Arcade", True, (10, 10, 10))
            textpos = text.get_rect(centerx=background.get_width() / 2, y=10)
            background.blit(text, textpos)

    def add_picture(self):
        """loads an image, prepares it for play"""
        try:
            surface = pg.image.load(self.image)
        except pg.error:
            raise SystemExit(f'Could not load image "{file}" {pg.get_error()}')
        return surface.convert()

    


