import pygame as pg
from pathlib import Path
from utils import load_image

class Arena:
    def __init__(self, image_path=None,display_caption=None, display_width=2000, 
                display_height=1200, text="", mouse_visible=False, color=None):
        self.image=image_path
        self.display_width = display_width
        self.display_height = display_height
        self.mouse_visible = mouse_visible
        self.color = color
        self.text = text
        self.display_caption=display_caption
        self.screen = pg.display.set_mode((self.display_width, self.display_height)) 

    def display(self):
        if self.display_caption:
            pg.display.set_caption(self.display_caption)
       
        self.background= self.create_background()      
        self.screen.blit(self.background, (0, 0))


    def create_background(self):
        self.background = pg.Surface(self.screen.get_size())
        if self.color:
            self.background.convert()
            self.background.fill(self.color)
        if self.image:
            try:
             self.background=pg.image.load(self.image).convert()
            except pg.error:
                raise SystemExit(f'Could not load image "{self.image}" {pg.get_error()}')
            self.screen = pg.display.set_mode((self.background.get_size()))
        if self.text:
            self.add_text()
        return self.background

     
       
       
        
    


