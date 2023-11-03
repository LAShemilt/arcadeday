import pygame as pg
from pathlib import Path


def load_and_scale( image_path, scale_factor):
    try:
        image = pg.image.load(image_path)
    except pg.error:
        raise SystemExit(f'Could not load image "{file}" {pg.get_error()}')
    size = image.get_size()
    size = (size[0] * scale_factor, size[1] * scale_factor)
    image = pg.transform.scale(image, size)
    return image

def config_reader(config):
    pass