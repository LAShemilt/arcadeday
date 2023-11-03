import pygame as pg
from pathlib import Path
import yaml
from munch import Munch

class Arena:
    def __init__(self, config , **kwargs):

        if config:
            self._attributes = self.read_config(config)
        elif kwargs:
            self._attributes = self.attributes(kwargs)

    @property
    def attributes(self):
        return self._attributes
    
    @attributes.setter
    def attributes(self, **kwargs):
        if kwargs:
                self._attributes.update(kwargs)
        
    @staticmethod
    def read_config(config):
        with open(config, 'r') as file:
            attributes = Munch(yaml.safe_load(file))
        return attributes

    def display(self):
        if self.attributes.display_caption:
            pg.display.set_caption(self.attributes.display_caption)
        self.background= self.create_background()      
        self.screen.blit(self.background, (0, 0))


    def create_background(self):
        self.screen = pg.display.set_mode((self.attributes.display_width, self.attributes.display_height)) 
        self.background = pg.Surface(self.screen.get_size())
        if self.attributes.color:
            self.background.convert()
            self.background.fill(self.attributes.color)
        if self.attributes.image_path:
            try:
             self.background=pg.image.load(Path("data").joinpath(self.attributes.image_path)).convert()
            except pg.error:
                raise SystemExit(f'Could not load image "{self.attributes.image_path}" {pg.get_error()}')
            self.screen = pg.display.set_mode((self.background.get_size()))

        return self.background

     
       
       
        
    


