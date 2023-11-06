# ArcadeDay
Welcome to ArcadeDay! This repo gives you the building blocks to start your game. 

# Getting started

Activate the conda environment `rfi-arcade`:
```conda activate rfi-arcade```


From a terminal , change directory to `pygame_templates` and run `python3 main.py`, a window will pop up and display a character. You will see a test tube falling from the sky. Use the left and right arrow keys to move the character and try and catch the test tube. 

This programme was built from the following 3 template files: `arena.py`, `sprites.py` and `main.py`and can be edited to make the basics of your game. 

There are two directories `data` and `configs` which can be used to change the aesthetics of your game with out programming. This will save you time to concentrate on the movement and interaction of your sprites. 

## Changing the Arena

`arena.py` can be changed through use of a config file. You do not have to update this code at all. 
You can either set up a custom arena or create an arena from an image. The config file, `arena_config.yml`, is set out with the following variables:

```
color: (0,0,0) # set RGB values up to 255 to set your background colour
image_path: imp.png # name of your image file
display_width: 2000 # display width in pixels
display_height: 400 # display height in pixels
display_caption: RFI-Arcade # display window caption
mouse_visible: False # If your game requires a mouse to play set to True, if not set to False

```
You can change the background by adding a file in jpg or png format into the data folder. arena.py will pick this up if you update the image_path variable in the config with the name of your file.
When using images the background will scale to the size of the image, so for best results try to go for a background that is around 1200x 500 pixels.


## Changing the sprite
You can change the sprite attributes and appearance by creating a config file and adding a new picture file (`jpg` or `png`) to the data folder. 

To make a new sprite, inherit the `SpriteConfig` class. You can then make a new sprite by adding a second config and a second picture to the data file. For more examples see the `TestTube` class in `sprites.py`

To set up a new sprite look at the example of `FranklinImp` in `sprites.py`:
```
class FranklinImp(SpriteConfig):
    """A little imp that saves your lab."""
    def __init__(self, config, **kwargs):
        super().__init__(config, **kwargs)
        self.direction = 1
    def update(self, direction):
        self.direction= direction
        self._walk()

    def _walk(self):
        newpos = self.rect.move((self.direction*self.move, 0))
        self.rect = newpos

    def jump(self):
        self.direction = -1*self.direction
        newpos = self.rect.move((0, self.direction*20 ))
        self.rect = newpos

    def your_methods():
        pass
```

The function `your_methods` shows you how you can extend the class to make your sprite move in the way you want it too. You can add motions to the class by creating functions such as:

```
def move_right(self):
    return self.position = self.position + 1
```


## Adding your game concept to `main.py`

The main.py script is where the game is launched  and executed. The structure of the script is in three parts: initialize the sprites and arena, designing the game loop, running the game.
In the main method you need to first initialize your game using the pg.init command. Then create instances of all your sprites and your background.  You then need to set up a clock that controls the frame rate of your game.

