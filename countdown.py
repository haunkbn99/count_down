import pygame
import time
from pygame import mixer

pygame.init()
pygame.font.init()

screen = pygame.display.set_mode((650,350))
pygame.display.set_caption('Count Down')

#set_front
font = pygame.font.SysFont('Commic Sans MS',30)
font_digit = pygame.font.SysFont("Trebuchet MS", 100)

#sound_file
sound_file = 'sound.wav'
#Color
GREY = (150,150,150)
BLACKGROUND = (74, 72, 68)
WHITE = (255,255,255)
GREEN_PASTEL = (150, 190, 140)
RED_PASTEL = (210, 110, 100)

#rectangel
RECT1 = (50,30,100,200)
RECT2 = (200,30,100,200)
RECT3 = (350,30,100,200)
RECT4 = (500,30,100,200)
RECT5 = (50,280,250,50)
RECT6 = (350,280,250,50)

#variable
total_hours = 0
total_mins = 0
total_secs = 0
total_milisecs = 0

#text
text1 = font.render('Start / Pause',True,WHITE)
text2 = font.render('Reset',True,WHITE)
text3 = font.render('hour',True,WHITE)
text4 = font.render('min',True,WHITE)
text5 = font.render('sec',True,WHITE)
text6 = font.render('milisec',True,WHITE)

#status_program
running = True
start_status = False

def countdown(hour,min,sec,milisec):
	if milisec > 0:
		milisec -= 1
		return hour,min,sec,milisec
	elif sec > 0:
		milisec = 59
		sec -= 1
		return hour,min,sec,milisec
	elif min > 0:
		milisec = 59
		sec = 59
		min -= 1
		return hour,min,sec,milisec
	elif hour > 0:
		milisec = 59
		sec = 59
		min = 59
		hour -=1
		return hour,min,sec,milisec
def countup(hour,min,sec):
	if sec == 60:
		sec = 0
		min += 1
		countup(hour,min,sec)
	if min == 60:
		min = 0
		if hour < 24:
			hour += 1
	return hour, min, sec


while running:

	screen.fill(BLACKGROUND)

	mouse_x, mouse_y = pygame.mouse.get_pos()

	pygame.draw.rect(screen,GREY,RECT1)
	pygame.draw.rect(screen,GREY,RECT2)
	pygame.draw.rect(screen,GREY,RECT3)
	pygame.draw.rect(screen,GREY,RECT4)
	pygame.draw.rect(screen,GREEN_PASTEL,RECT5)
	pygame.draw.rect(screen,RED_PASTEL,RECT6)

	if start_status:
		if (total_hours,total_mins,total_secs,total_milisecs) == (0,0,0,0):
			start_status = False
			mixer.init()
			mixer.music.load(sound_file)
			mixer.music.play()
		else:
			total_hours, total_mins,total_secs,total_milisecs = countdown(total_hours,total_mins,total_secs,total_milisecs)
			time.sleep(1/60)

	text_hours = font_digit.render(str(total_hours),True,WHITE)
	text_mins  = font_digit.render(str(total_mins),True,WHITE)
	text_secs  = font_digit.render(str(total_secs),True,WHITE)
	text_milisecs = font_digit.render(str(total_milisecs),True,WHITE)

	screen.blit(text1,(120,300))
	screen.blit(text2,(450,300))
	screen.blit(text3,(80,240))
	screen.blit(text4,(230,240))
	screen.blit(text5,(380,240))
	screen.blit(text6,(515,240))
	screen.blit(text_hours,(60,100))
	screen.blit(text_mins,(210,100))
	screen.blit(text_secs,(360,100))
	screen.blit(text_milisecs,(510,100))
	# print((mouse_x,mouse_y))

	for event in pygame.event.get():
		#stop music alarm
		if event.type == pygame.MOUSEBUTTONDOWN:
			mixer.music.stop()
		#quit program
		if event.type == pygame.QUIT:
			running = False
		#start_button
		if event.type == pygame.MOUSEBUTTONDOWN:
			if (event.button ==1 and 50<mouse_x and mouse_x<300 and 280<mouse_y and mouse_y<330):
				print("Start")
				if start_status == False:
					start_status = True
				else:
					start_status = False
		#reset_button
		if event.type == pygame.MOUSEBUTTONDOWN:
			if (event.button ==1 and 350<mouse_x and mouse_x<600 and 280<mouse_y and mouse_y<330):
				total_hours = 0
				total_mins = 0
				total_secs = 0
				total_milisecs = 0
				start_status = False
				print("Reset")
		#hour_botton
		if event.type == pygame.MOUSEBUTTONDOWN:
			if (event.button ==1 and 50<mouse_x and mouse_x<150 and 30<mouse_y and mouse_y<230):
				if total_hours < 24:
					total_hours += 1
				start_status = False
		#min_botton
		if event.type == pygame.MOUSEBUTTONDOWN:
			if (event.button ==1 and 200<mouse_x and mouse_x<300 and 30<mouse_y and mouse_y<230):
				total_mins += 1
				total_hours,total_mins,total_secs = countup(total_hours,total_mins,total_secs)
				start_status = False
		#sec_botton
		if event.type == pygame.MOUSEBUTTONDOWN:
			if (event.button ==1 and 350<mouse_x and mouse_x<450 and 30<mouse_y and mouse_y<230):
				total_secs += 1
				total_hours,total_mins,total_secs = countup(total_hours,total_mins,total_secs)
				start_status = False

	pygame.display.flip()
pygame.quit()