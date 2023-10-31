import pygame as pg
from pathlib import Path


def load_image(fpath):
    """loads an image, prepares it for play"""
    try:
        surface = pg.image.load(fpath)
    except pg.error:
        raise SystemExit(f'Could not load image "{file}" {pg.get_error()}')
    return surface


def load_and_scale( image_path, scale_factor):
    image = pg.image.load(image_path)
    size = image.get_size()
    size = (size[0] * scale_factor, size[1] * scale_factor)
    image = pg.transform.scale(image, size)
    return image
