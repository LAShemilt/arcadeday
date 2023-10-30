import pygame as pg
from pathlib import Path
from utils import load_image

class Background:
    def __init__(self, image_path=None,display_caption=None, display_width=800, 
                display_height=400, text="", mouse_visible=False, color=None, scaled=False):
        self.image=image_path
        self.display_width = display_width
        self.display_height = display_height
        self.mouse_visible = mouse_visible
        self.color = color
        self.text = text
        self.display_caption=display_caption
        self.scaled = scaled
        self.screen = pg.display.set_mode((self.display_width, self.display_height), pg.SCALED) 

    def display(self):
        if self.display_caption:
            pg.display.set_caption(self.display_caption)
       
        self.background= self.create_background()      
        self.screen.blit(self.background, (0, 0))
        pg.display.flip()

    def create_background(self):
        self.background = pg.Surface(self.screen.get_size())
        if self.color:
            if self.scaled:
              self.screen = pg.display.set_mode((self.display_width, self.display_height), pg.SCALED)
            self.background.convert()
            self.background.fill(self.color)
        if self.image:
            self.background=pg.image.load(self.image).convert()
            if self.scaled:
                self.screen = pg.display.set_mode((self.background.get_size()), pg.SCALED)
            else:
                self.screen = pg.display.set_mode((self.background.get_size()))
        if self.text:
            self.add_text()
        return self.background

    def add_text(self):

        # Put Text On The Background, Centered
        if pg.font:
            font = pg.font.Font(None, 64)
            text = font.render(self.text, True, (10, 10, 10))
            textpos = text.get_rect(centerx=self.background.get_width() / 2, y=10)
            self.background.blit(text, textpos)

  
       
     
       
       
        
    


