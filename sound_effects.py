import pygame

pygame.mixer.init()

bullet_sound = pygame.mixer.Sound('sounds/laser1.wav')
alien_sound = pygame.mixer.Sound('sounds/explosion.wav')

# set volume of sound
bullet_sound.set_volume(0.2)
alien_sound.set_volume(0.2)