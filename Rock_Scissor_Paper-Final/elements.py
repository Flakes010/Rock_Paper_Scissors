import pygame
from os.path import join
from constants_lists import *

pygame.mixer.init()

game_music = pygame.mixer.Sound(join('assets', 'game_music.wav'))
game_music.set_volume(0.2)

accept_red = 0
accept_green = 0.2
accept_red2 = 0
accept_green2 = 1


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rock Scissors Paper")
clock = pygame.time.Clock()

rock = pygame.image.load(join('assets', 'rock.png'))
rock = pygame.transform.scale(rock, (SIZE,SIZE))
rock_sound = pygame.mixer.Sound(join('assets', 'rock_sound.wav'))

paper = pygame.image.load(join('assets', 'paper.png'))
paper = pygame.transform.scale(paper, (SIZE,SIZE))
paper_sound = pygame.mixer.Sound(join('assets', 'paper_sound.wav'))

scissors = pygame.image.load(join('assets', 'scissors.png'))
scissors = pygame.transform.scale(scissors, (SIZE,SIZE))
scissors_sound = pygame.mixer.Sound(join('assets', 'scissors_sound.wav'))

bg = pygame.image.load(join('assets', 'BG.jpg'))
bg = pygame.transform.scale(bg, (WIDTH, HEIGHT))
bg.set_alpha(128)

black = pygame.image.load(join('assets', 'black.png'))
black = pygame.transform.scale(black, (WIDTH, HEIGHT))

text_rockpaper = pygame.image.load(join('assets', 'rock_paper_text.png'))
text_scissors = pygame.image.load(join('assets', 'scissors_text.png'))

text_kadirihsan = pygame.image.load(join('assets', 'kadir_ihsan.png'))
text_github = pygame.image.load(join('assets', 'github.png'))
text_github_rect = text_github.get_rect()
text_github_rect.x = WIDTH//2-130
text_github_rect.y = 330

text_music = pygame.image.load(join('assets', 'MUSIC.png'))
text_sfx = pygame.image.load(join('assets', 'SFX.png'))

text_on = pygame.image.load(join('assets', 'ON.png'))
text_on_rect = text_on.get_rect()
text_on_rect.topleft = (420,150)

text_on2 = text_on.copy()
text_on2_rect = text_on2.get_rect()
text_on2_rect.topleft = (420,230)

text_off = pygame.image.load(join('assets', 'OFF.png'))
text_off_rect = text_off.get_rect()
text_off_rect.topleft = (555,150)

text_off2 = text_off.copy()
text_off2_rect = text_off2.get_rect()
text_off2_rect.topleft = (555,230)

green_box = pygame.image.load(join('assets', 'GREEN.png'))
green_box_rect = green_box.get_rect()
green_box_rect.topleft = (410,145)

green_box2 = green_box.copy()
green_box2_rect = green_box2.get_rect()
green_box2_rect.topleft = (410,225)

red_box = pygame.image.load(join('assets', 'RED.png'))
red_box_rect = red_box.get_rect()
red_box_rect.topleft = (550,145)

red_box2 = red_box.copy()
red_box2_rect = red_box2.get_rect()
red_box2_rect.topleft = (550,225)