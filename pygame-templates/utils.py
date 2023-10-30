import pygame as pg
from pathlib import Path


def load_image(fpath):
    """loads an image, prepares it for play"""
    try:
        surface = pg.image.load(fpath)
    except pg.error:
        raise SystemExit(f'Could not load image "{file}" {pg.get_error()}')
    return surface