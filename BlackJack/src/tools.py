import os
import pygame
from . import setup


def load_images(path):
    images = {}
    for image in os.listdir(path):
        # Name of file without the . and file type
        image_name = image.split(".")[0]
        temp_image = pygame.image.load(path + "/" + image)
        images[image_name] = scale_image(temp_image, image_name)

    return images


def scale_image(image, name):
    # Scale chip images accordingly
    if 'chip' in name:
        return pygame.transform.scale(image, (setup.CHIP_WIDTH, setup.CHIP_HEIGHT))
    else:
        return image


def load_sounds(path):
    sounds = {}
    for sound in os.listdir(path):
        sound_name = sound.split(".")[0]
        sounds[sound_name] = pygame.mixer.Sound(path + "/" + sound)
    return sounds