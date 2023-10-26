# Pygame Templates
Welcome to pygame templates! This repo gives you the building blocks to start your game. 

# Getting starteded

Activate the conda environment `rfi-arcade`:
```conda activate rfi-arcade```


If you run `mygame` from the console, a window will pop up and display a character. Click on the character and see what happens.

This programe was built from the following 3 template files: `background.py`, `sprites.py` and `main.py`and can be edited to make the basics of your game. 

## Changing the background

You can change the background by adding a different `background.png` file into the `data` folder. The `background.py` file will pick this up and change the sprite. If you want to change the screen size please edit the background config variables `SCREEN_WIDTH`, `SCREEN_HEIGHT`.

## Changing the sprite
You can change the sprite by adding a different `sprite.png` file into the `data` folder. The `sprite.py` file will pick this up and change the sprite. 

To make a new sprite, inherit the `SpriteBase` class. You can add your own picture to the sprite by changing the filename attribute to have a different file name.

You can add motions to the class by creating functions such as:

```
def move_right(self):
    return self.position = self.position + 1
```


## Adding your game concept to `main.py`
