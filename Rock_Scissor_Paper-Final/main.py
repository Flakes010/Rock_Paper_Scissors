import pygame
from sys import exit
from os.path import join
from random import randint
import math
import os
from webbrowser import open
from elements import *
from constants_lists import *


pygame.init()

class Object(pygame.sprite.Sprite):
    def __init__(self, x, y, size, mode):
        super().__init__()

        self.x = x
        self.y = y
        self.mode = mode
        self.image = pygame.image.load(join('assets', '{}.png'.format(mode)))
        self.image = pygame.transform.scale(self.image, (size, size))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    
    def change_mode(self, mode):
        if self.mode == 'rock': rock_group.remove(self)
        elif self.mode == 'scissors': scissors_group.remove(self)
        elif self.mode == 'paper': papers_group.remove(self)
        self.mode = mode
        if mode == 'rock': rock_group.append(self)
        elif mode == 'scissors': scissors_group.append(self)
        elif mode == 'paper': papers_group.append(self)
        self.image = pygame.image.load(join('assets', '{}.png'.format(mode)))
        self.image = pygame.transform.scale(self.image, (SIZE, SIZE))

    def show_object(self, mode):
        self.image = pygame.image.load(join('assets', '{}{}.png'.format('selected_', mode)))
        self.image = pygame.transform.scale(self.image, (SIZE, SIZE))

    def follow_object(self, coords):
        start_x = self.rect.x
        start_y = self.rect.y

        dest_x = coords[0]
        dest_y = coords[1]

        x_diff = dest_x - start_x
        y_diff = dest_y - start_y
        angle = math.atan2(y_diff, x_diff)

        self.change_x = math.cos(angle) * SPEED
        self.change_y = math.sin(angle) * SPEED

        self.rect.x += self.change_x
        self.rect.y += self.change_y
    

class Button:
	def __init__(self,text,width,height,pos,elevation):
		#Core attributes 
		self.pressed = False
		self.elevation = elevation
		self.dynamic_elecation = elevation
		self.original_y_pos = pos[1]
 
		# top rectangle 
		self.top_rect = pygame.Rect(pos,(width,height))
		self.top_color = '#475F77'
 
		# bottom rectangle 
		self.bottom_rect = pygame.Rect(pos,(width,height))
		self.bottom_color = '#354B5E'
		# text
		self.text = text
		self.text_surf = gui_font.render(text,True,'#FFFFFF')
		self.text_rect = self.text_surf.get_rect(center = self.top_rect.center)
 
	def change_text(self, newtext):
		self.text_surf = gui_font.render(newtext, True,'#FFFFFF')
		self.text_rect = self.text_surf.get_rect(center = self.top_rect.center)
 
	def draw(self):
		# elevation logic 
		self.top_rect.y = self.original_y_pos - self.dynamic_elecation
		self.text_rect.center = self.top_rect.center 
 
		self.bottom_rect.midtop = self.top_rect.midtop
		self.bottom_rect.height = self.top_rect.height + self.dynamic_elecation
 
		pygame.draw.rect(screen,self.bottom_color, self.bottom_rect,border_radius = 12)
		pygame.draw.rect(screen,self.top_color, self.top_rect,border_radius = 12)
		screen.blit(self.text_surf, self.text_rect)
 
	def check_click(self):
		mouse_pos = pygame.mouse.get_pos()
		if self.top_rect.collidepoint(mouse_pos):
			self.top_color = '#D74B4B'
			if pygame.mouse.get_pressed()[0]:
				self.dynamic_elecation = 0
				self.pressed = True
				self.change_text(f"{self.text}")
			else:
				self.dynamic_elecation = self.elevation
				if self.pressed == True:
					self.pressed = False
					self.change_text(self.text)
					return True
		else:
			self.dynamic_elecation = self.elevation
			self.top_color = '#475F77'

def create_objects():
    for i in range(NUMBER):
        rock = Object(randint(50,650), randint(50,650), SIZE, "rock")
        group.add(rock)
        rock_group.append(rock)
        scissors = Object(randint(50,650), randint(50,650), SIZE, "scissors")
        group.add(scissors)
        scissors_group.append(scissors)
        paper = Object(randint(50,650), randint(50,650), SIZE, "paper")
        group.add(paper)
        papers_group.append(paper)


def delete_objects():
    for i in group:
        i.kill()
    rock_group.clear()
    scissors_group.clear()
    papers_group.clear()


def control():
    if len(scissors_group) == 0 and len(papers_group) == 0:
        return False
    elif len(scissors_group) == 0 and len(rock_group) == 0:
        return False
    elif len(rock_group) == 0 and len(papers_group) == 0:
        return False


def clear(object):
    object.center = (1000, 1000)


gui_font = pygame.font.Font(None, 30)
game_font = pygame.font.Font(None, 30)

menu_button = Button('Start', 200, 40, (WIDTH//2-100,360), 5)
options_button = Button('Options', 200, 40, (WIDTH//2-100,440), 5)
credits_button = Button('Credits', 200, 40, (WIDTH//2-100,520), 5)
back_button = Button('Back', 120, 40, (40, 630), 5)
end_button = Button('End!',200,40,(WIDTH//2, HEIGHT//2),5)
show_data_button = Button('Show Data',150,35,(530, 650),5)


def main():
    show_data = False
    running = True
    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                exit()

        screen.fill((30,30,30))
        group.draw(screen)

        for object in group:
            object.rect.x += randint(-1,1)
            object.rect.y += randint(-1,1)

            if object in papers_group:
                for rock in rock_group:
                    red_coord1 = (object.rect.x, object.rect.y)
                    red_coord2 = (rock.rect.x, rock.rect.y) # target coords
                if show_data: pygame.draw.line(screen, (255,0,0), red_coord1, red_coord2)
                object.follow_object(red_coord2)
                
            
            if object in rock_group:
                for scissor in scissors_group:
                    green_coord1 = (object.rect.x, object.rect.y)
                    green_coord2 = (scissor.rect.x, scissor.rect.y)
                if show_data: pygame.draw.line(screen, (0,255,0),  green_coord1, green_coord2)
                object.follow_object(green_coord2)
                

            if object in scissors_group:
                for paper in papers_group:
                    blue_coord1 = (object.rect.x, object.rect.y)
                    blue_coord2 = (paper.rect.x, paper.rect.y)
                if show_data: pygame.draw.line(screen, (0,0,255),  blue_coord1, blue_coord2)
                object.follow_object(blue_coord2)


            if object.rect.right >= WIDTH:
                object.rect.x -= 3
            elif object.rect.left <= 0:
                object.rect.x += 3
            if object.rect.bottom >= HEIGHT:
                object.rect.y -= 3
            elif object.rect.top <= 0:
                object.rect.x += 3

            for i in group:
                if object.rect.colliderect(i):
                    if object.mode == "scissors" and i.mode == "paper":
                        i.change_mode("scissors")
                        if accept_green2:
                            scissors_sound.play()
                    if object.mode == "paper" and i.mode == "rock":
                        i.change_mode("paper")
                        if accept_green2:
                            paper_sound.play()
                    if object.mode == "rock" and i.mode == "scissors":
                        i.change_mode("rock")
                        if accept_green2:    
                            rock_sound.play()

        if show_data_button.check_click():
            if show_data == False:
                show_data = True
                show_data_button.change_text("Hide Data")
            elif show_data:
                show_data = False
                show_data_button.change_text("Show Data")

        if control() == False:
            end_button.draw()
            if end_button.check_click():
                screen.fill((30,30,30))
                delete_objects()
                create_objects()
                menu()
        else: show_data_button.draw()
        
        pygame.display.update()


def menu():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        
        screen.blit(black, (0,0))

        screen.blit(bg, (0,0))

        menu_button.draw()
        options_button.draw()
        credits_button.draw()

        screen.blit(text_rockpaper, (WIDTH//2-210,120))
        screen.blit(text_scissors, (WIDTH//2-170,200))

        if menu_button.check_click(): main()
            
        if options_button.check_click(): options()
            
        if credits_button.check_click(): credits()
            
        pygame.display.update()
        clock.tick(FPS)


def credits():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if text_github_rect.collidepoint(x, y):
                    open(URL)
        
        screen.blit(black, (0,0))

        screen.blit(bg, (0,0))

        back_button.draw()

        screen.blit(text_kadirihsan, (WIDTH//2-220,250))
        screen.blit(text_github, (WIDTH//2-130,330))

        if back_button.check_click(): menu()
            
        pygame.display.update()
        clock.tick(FPS)


def options():
    global accept_red, accept_green, accept_red2, accept_green2
    
    while True:
        game_music.set_volume(accept_green)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos

                if text_off_rect.collidepoint(x, y):
                    accept_red = 1
                    accept_green = 0
                if text_on_rect.collidepoint(x, y):
                    accept_green = 0.2
                    accept_red = 0
                    
                if text_off2_rect.collidepoint(x, y):
                    accept_red2 = 1
                    accept_green2 = 0
                if text_on2_rect.collidepoint(x, y):
                    accept_green2 = 1
                    accept_red2 = 0
        
        screen.blit(black, (0,0))

        screen.blit(bg, (0,0))

        back_button.draw()

        screen.blit(text_music, (50,150))

        if accept_green: screen.blit(green_box, (410,145))
        screen.blit(text_on, (420,150))
        if accept_red: screen.blit(red_box, (550,145))
        screen.blit(text_off, (555,150))
        screen.blit(text_sfx, (50,230))
        if accept_green2: screen.blit(green_box2, (410,225))
        screen.blit(text_on2, (420,230))
        if accept_red2: screen.blit(red_box2, (550,225))
        screen.blit(text_off2, (555,230))

        if back_button.check_click(): menu()
            
        pygame.display.update()
        clock.tick(FPS)



if __name__ == "__main__":
    file_path = os.path.dirname(os.path.abspath(__file__))
    os.chdir(file_path)

    create_objects()
    game_music.play(-1)
    menu()

pygame.quit()