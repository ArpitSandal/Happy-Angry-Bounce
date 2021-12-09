import pygame
import random

#initialize the pygame
pygame.init()

#create the screen
screen=pygame.display.set_mode((800,600)) # (x,y)
#bounce back is 736 and 536

#title and icon
pygame.display.set_caption("Happy-Angry Bounce")
icon=pygame.image.load("smiling.png")
pygame.display.set_icon(icon)


#my image
emojihappy=pygame.image.load("image.png")
emojiangry=pygame.image.load("angry.png")
emojix=random.randint(100,370) #x coordinate of my image
emojiy=random.randint(130,270) #y coordinate of my image


#Dynamics for my image
addx=0.2 #moving at the rate of 0.2 pixel
addy=0.2


#function diplaying my image
def emojifun():
	screen.blit(emojihappy,(emojix,emojiy))


#everything in my screen will be controlled from here
running=True
while running:
	#filling the screen with the required colour, R-G-B(Red,Green,Blue...max_value==255) 
	screen.fill((254,254,254))


	#Displaying my image on the screen
	emojifun()


    #going through all the events in pygame
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			running=False
		
		#keypresses for the image
		if event.type==pygame.KEYDOWN:
			if event.key==pygame.K_LEFT:
				addx=-addx
			elif event.key==pygame.K_RIGHT:
				addx=-addx
			if event.key==pygame.K_UP:
				addy=-addy
			elif event.key==pygame.K_DOWN:
				addy=-addy


	#increasing the x and y coordinate of out image
	emojix+=addx
	emojiy+=addy


	#Bounce Back conditions
	if emojix<=0 or emojix>=736:
		addx=-addx
		emojihappy,emojiangry=emojiangry,emojihappy #swapping the face on each bounce back
	elif emojiy<=0 or emojiy>=536:
		addy=-addy
		emojihappy,emojiangry=emojiangry,emojihappy #swapping the face on each bounce back


	#updating our display
	pygame.display.update()