import pygame as pg
from utils import load_and_scale, read_config
from pathlib import Path

class FranklinImp(pg.sprite.Sprite):
    """A little imp that destroys your lab."""

    def __init__(self, config, **kwargs):
        pg.sprite.Sprite.__init__(self)

        if config:
            self._attributes = read_config(config)
        elif kwargs:
            self._attributes = self.attributes(kwargs)

        self.image = load_and_scale(Path("data").joinpath(self.attributes.image_path), self.attributes.scale)
        self.rect = self.image.get_rect()
        self.rect.center = (self.attributes.start_pos[0], self.attributes.start_pos[1])
        self.move = self.attributes.move
        screen = pg.display.get_surface()
        self.area = screen.get_rect()

    @property
    def attributes(self):
        return self._attributes
    
    @attributes.setter
    def attributes(self, **kwargs):
        if kwargs:
                self._attributes.update(kwargs)
    
    def update(self):
        self._walk()

    def _walk(self):
        newpos = self.rect.move((self.move, 0))
        self.rect = newpos

    def your_methods():
        pass


# class TestTube(pg.sprite.Sprite):
#     """Exploding testubes."""

    

#     def __init__(self, *groups):
#         pg.sprite.Sprite.__init__(self, *groups)
#         self.image = self.images[0]
#         self.rect = self.image.get_rect()
  

#     def update(self):
#         if self.explode:

#     def explode(self):
#          newpos = self.rect.move((self.move, 0))
#         if not self.area.contains(newpos):
#             if self.rect.left < self.area.left or self.rect.right > self.area.right:
#                 self.move = -self.move
#                 newpos = self.rect.move((self.move, 0))
#                 self.image = pg.transform.flip(self.image, True, False)
#         self.rect = newpos

#     def your_methods():
#         pass

