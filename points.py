# coding=UTF-8
'''
Created on 10 févr. 2015

@author: pclf
'''

import vectors
import gstt
import random
import globalVars
import pylibmc

mc = pylibmc.Client(["127.0.0.1"], binary=True, behaviors={"tcp_nodelay": True, "ketama": True})


LOGO = [
	# Etoile
	[[(-155,-95),(-135,-85)],0xFF00],
	[[(-155,-85),(-135,-95)],0xFF00],
	[[(-150,-100),(-140,-80)],0xFF00],
	# L/o
	[[(-140,-100),(-200,20),(120,20)],0xFF00],
	# aser
	[[(-140,-40),(-100,-40,),(-120,0),(-160,0),(-110,-20)],0xFFFF],
	[[(-40,-40),(-60,-40),(-90,-20),(-50,-20),(-80,0),(-100,0)],0xFFFF],
	[[(-30,-20),(10,-20),(0,-40),(-20,-40),(-30,-20),(-30,0),(-10,0)],0xFFFF],
	[[(20,0),(40,-40),(35,-30),(50,-40),(70,-40)],0xFFFF],
	]

#LOGO_OFFSET = vectors.Vector2D(200,-100)
LOGO_OFFSET = vectors.Vector2D(400,320)
screen_size = [850,600]

def Draw(f):

	c = 0xFFFF
	xy_list = []
	
	print mc["some_key"]
	
	xrand = random.randint(-screen_size[0]/2, screen_size[0]/2)
	yrand = random.randint(-screen_size[1]/2, screen_size[1]/2)
	xy_list.append((LOGO_OFFSET + vectors.Vector2D(xrand,yrand)).ToTuple())
	
	xy_list.append((LOGO_OFFSET + vectors.Vector2D(xrand+1,yrand+1)).ToTuple())
	
	f.PolyLineOneColor(xy_list, c)
	
	



