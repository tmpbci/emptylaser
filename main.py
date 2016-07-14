# coding=UTF-8
'''
Empty Laser 
By Sam Neurohack
LICENCE : CC

You get a basic pygame skeleton to handle the laser drawing with an onscreen simulator.
This Empty Laser is mainly a Laser Hexagon (see /tmp/lab github) structure with some extras, like alignement keys.

Many things are still in the todo list as how to store the align parameters in globalVars for the next run.

'''


import pygame

# STDLIB
import math
import random
import itertools
import sys
import os
import thread
import time

from globalVars import *
import gstt
import playertest
import harp
import points
import score
import logo
import pylibmc

mc = pylibmc.Client(["127.0.0.1"], binary=True, behaviors={"tcp_nodelay": True, "ketama": True})

import frame
from vectors import Vector2D
import renderer
import dac



def StartPlaying(first_time = False):
	gstt.score.Reset()
	gstt.fs = GAME_FS_PLAY

	
def dac_thread():

	while True:
		try:

			d = dac.DAC(dac.find_first_dac())
			d.play_stream(laser)

		except Exception as e:

			import sys, traceback
			print '\n---------------------'
			print 'Exception: %s' % e
			print '- - - - - - - - - - -'
			traceback.print_tb(sys.exc_info()[2])
			print "\n"
			pass

def DrawTestPattern(f):
	l,h = screen_size
	L_SLOPE = 30
	
	f.Line((0, 0), (l, 0), 0xFFFFFF)
	f.LineTo((l, h), 0xFFFFFF)
	f.LineTo((0, h), 0xFFFFFF)
	f.LineTo((0, 0), 0xFFFFFF)
	
	f.LineTo((2*L_SLOPE, h), 0)
	for i in xrange(1,7):
		c = (0xFF0000 if i & 1 else 0) | (0xFF00 if i & 2 else 0) | (0xFF if i & 4 else 0)
		f.LineTo(((2 * i + 1) * L_SLOPE, 0), c)
		f.LineTo(((2 * i + 2) * L_SLOPE, h), c)
	f.Line((l*.5, h*.5), (l*.75, -h*.5), 0xFF00FF)
	f.LineTo((l*1.5, h*.5), 0xFF00FF)
	f.LineTo((l*.75, h*1.5), 0xFF00FF)
	f.LineTo((l*.5, h*.5), 0xFF00FF)
		
def Align(f):
	l,h = screen_size
	L_SLOPE = 30
	
	f.Line((0, 0), (l, 0), 0xFFFFFF)
	f.LineTo((l, h), 0xFFFFFF)
	f.LineTo((0, h), 0xFFFFFF)
	f.LineTo((0, 0), 0xFFFFFF)
	laser = renderer.LaserRenderer(fwork_holder, gstt.centerx, gstt.centery, gstt.zoomx, gstt.zoomy, gstt.sizex, gstt.sizey)

	print str(gstt.centerx) + "," + str(gstt.centery) + "," + str(gstt.zoomx) + "," + str(gstt.zoomy) + "," + str(gstt.sizex) + "," + str(gstt.sizey)
	

app_path = os.path.dirname(os.path.realpath(__file__))

pygame.init()

screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Empty Laser")
clock = pygame.time.Clock()

gstt.centerx = LASER_CENTER_X
gstt.centery = LASER_CENTER_Y
gstt.zoomx = LASER_ZOOM_X
gstt.zoomy = LASER_ZOOM_Y
gstt.sizex = LASER_SIZE_X
gstt.sizey = LASER_SIZE_Y
gstt.finangle = LASER_ANGLE

fwork_holder = frame.FrameHolder()
laser = renderer.LaserRenderer(fwork_holder, gstt.centerx, gstt.centery, gstt.zoomx, gstt.zoomy, gstt.sizex, gstt.sizey)


current_string = 0 

thread.start_new_thread(dac_thread, ())


update_screen = False

gstt.score = score.Score()
gstt.plyr = playertest.PlayerTest()
gstt.hrp = harp.Harp()

keystates = pygame.key.get_pressed()

gstt.fs = GAME_FS_MENU
gstt.opened = 0
gstt.space = 1
gstt.opening = 0
gstt.closed = 1
gstt.closing = 0

while gstt.fs != GAME_FS_QUIT:

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			gstt.fs = GAME_FS_QUIT
	
	keystates_prev = keystates[:]
	keystates = pygame.key.get_pressed()[:]

# Code commun de test selon etats du jeu



	if gstt.fs == GAME_FS_MENU:
		if keystates[pygame.K_ESCAPE] and not keystates_prev[pygame.K_ESCAPE]:
			gstt.fs = GAME_FS_QUIT
		elif keystates[pygame.K_SPACE] and not keystates_prev[pygame.K_SPACE]:
			StartPlaying(True)
			
		if gstt.closed == 0:
			print "gstt.closed : ", gstt.closed, "gstt.space : ", gstt.space
			gstt.space -= 10
			if gstt.space < 0:
				gstt.closed = 1 
					
			gstt.hrp.Color(current_string,0)
			current_string += 1
			if current_string > 8:
				current_string = 0 



	elif gstt.fs == GAME_FS_PLAY:
	
	# Escape vers menu
		if keystates[pygame.K_ESCAPE] and not keystates_prev[pygame.K_ESCAPE]:
			gstt.fs = GAME_FS_MENU
			gstt.opened = 1
			gstt.closed = 0
			gstt.space = 250

	# anim harp
		if gstt.opened == 0:
			gstt.opening += 1
			if gstt.opening== 1:
				gstt.space += 3
				gstt.opening= 0
				if gstt.space == 250:
					gstt.opened = 1 
		
		gstt.hrp.Color(current_string,0)
		current_string += 1
		if current_string > 8:
			current_string = 0 
	
	# anim playertest
		up_key = keystates[pygame.K_UP]
		down_key = keystates[pygame.K_DOWN]
		left_key = keystates[pygame.K_LEFT]
		right_key = keystates[pygame.K_RIGHT]
		
		gstt.plyr.Move(up_key,down_key,left_key,right_key)
		


		

	elif gstt.fs == GAME_FS_GAMEOVER:

		if keystates[pygame.K_SPACE] and not keystates_prev[pygame.K_SPACE]:
			StartPlaying(False)
			gstt.opened = 0
			gstt.space = 1
			gstt.opening= 0
		elif keystates[pygame.K_ESCAPE] and not keystates_prev[pygame.K_ESCAPE]:
			gstt.fs = GAME_FS_MENU
		



	# OPERATIONS D'AFFICHAGE

	# On efface l'ecran avant
	screen.fill(0)

	# Création de la nouvelle frame vide où les objets du jeu vont dessiner
	fwork = frame.Frame()
	
	# Gestion de l'affichage du bord selon les touches de clavier pour s'aligner.
	if keystates[pygame.K_p]:
		DrawTestPattern(fwork)
		
	if keystates[pygame.K_x]:
		Align(fwork)
		
	if keystates[pygame.K_r]:
		gstt.centerx += 20
		Align(fwork)

	if keystates[pygame.K_t]:
		gstt.centerx -= 20
		Align(fwork)
		
	if keystates[pygame.K_y]:
		gstt.centery += 20
		Align(fwork)

	if keystates[pygame.K_u]:
		gstt.centery -= 20
		Align(fwork)

	if keystates[pygame.K_f]:
		gstt.zoomx += 0.1
		Align(fwork)

	if keystates[pygame.K_g]:
		gstt.zoomx -= 0.1
		Align(fwork)
		
	if keystates[pygame.K_h]:
		gstt.zoomy += 0.1
		Align(fwork)

	if keystates[pygame.K_j]:
		gstt.zoomy -= 0.1
		Align(fwork)
	
	if keystates[pygame.K_c]:
		gstt.sizex -= 50
		Align(fwork)
		
	if keystates[pygame.K_v]:
		gstt.sizex += 50
		Align(fwork)
		
	if keystates[pygame.K_b]:
		gstt.sizey -= 50
		Align(fwork)
		
	if keystates[pygame.K_n]:
		gstt.sizey += 50
		Align(fwork)
		
	if keystates[pygame.K_l]:
		gstt.finangle -= 0.001
		Align(fwork)
		
	if keystates[pygame.K_m]:
		gstt.finangle += 0.001
		Align(fwork)

	else:
		display_plyr = gstt.fs == GAME_FS_PLAY or gstt.fs == GAME_FS_GAMEOVER
		if display_plyr:
			gstt.plyr.Draw(fwork)
			gstt.hrp.Draw(fwork)
			
		if gstt.fs == GAME_FS_MENU:
			#logo.Draw(fwork)
			gstt.opened = 0
			#gstt.space = 1
	
			if gstt.closed == 1:
				gstt.space = 1
				logo.Draw(fwork)
				points.Draw(fwork)
				mc["some_key"] = str(random.randint(0,100))
			else:
				gstt.hrp.Draw(fwork)
			

	
	# Affecter la frame construite à l'objet conteneur de frame servant au système de rendu par laser
	fwork_holder.f = fwork

	if update_screen:
		update_screen = False
		fwork.RenderScreen(screen)
		pygame.display.flip()
	else:
		update_screen = True

	
	# TODO : rendre indépendante la fréquence de rafraîchissement de l'écran par
	# rapport à celle de l'animation du jeu
	clock.tick(100)

pygame.quit()


