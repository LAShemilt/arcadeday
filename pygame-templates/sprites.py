import pygame as pg

class FranklinImp(pg.sprite.Sprite):
    """A little imp that destroys your lab."""

    def __init__(self,image_path=None):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(image_path).convert()
        self.rect = self.image.get_rect()
        self.move = 10
        screen = pg.display.get_surface()
        self.area = screen.get_rect()
        self.rect.topleft = 10, 90
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

