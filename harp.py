# -*- coding: utf-8 -*-

from globalVars import *
import frame
import time
import vectors
import random
import gstt

SPEED = 4
SIZE = 20
bordersize = STRING_SIZE
HARP_OFFSET = vectors.Vector2D(0,0)



class Harp(object):
	
	def __init__(self):
		self.x, self.y = screen_size[0]/2, (screen_size[1]/2) + 100
		self.space = space
		self.strings = strings
		self.coloron =  COLOR_ON
		self.coloroff = COLOR_OFF
		self.scolors = [COLOR_OFF] * self.strings
		self.ssize = STRING_SIZE
		
	def Open(self,strings,space):
		for i in range (60):
			#print i
			gstt.hrp.Move(strings,i)
			time.sleep(0.007)
	
	def Color(self,string,color):
			self.scolors[string] = colorshex[color]
	
				
	def Change(self,string):
			if self.scolors[string] == COLOR_OFF:
				self.scolors[string] = COLOR_ON
			else:
				self.scolors[string] = COLOR_OFF

				
	def Event(self,string,state):
			if state == 0:
				self.scolors[string] = COLOR_OFF
			else:
				self.scolors[string] = COLOR_ON


	def Move(self,strings,space):
		self.strings = strings


	def Draw(self,f):
		xstart = self.x + random.randint(0,10) - ((self.strings / 2) * gstt.space) 
		self.ssize = STRING_SIZE - random.randint(0,10)
		bordersize = STRING_SIZE + 20
		
		LOGO = [
		
		[[(xstart, self.y),((xstart + bordersize),self.y)],self.scolors[0]],
		[[((xstart + gstt.space),self.y),((xstart + gstt.space + self.ssize),self.y)],self.scolors[1]],
		[[((xstart + gstt.space*2),self.y),((xstart + gstt.space*2 + self.ssize),self.y)],self.scolors[2]],
		[[((xstart + gstt.space*3),self.y),((xstart + gstt.space*3 + self.ssize),self.y)],self.scolors[3]],
		[[((xstart + gstt.space*4),self.y),((xstart + gstt.space*4 + self.ssize),self.y)],self.scolors[4]],
		[[((xstart + gstt.space*5),self.y),((xstart + gstt.space*5 + self.ssize),self.y)],self.scolors[5]],
		[[((xstart + gstt.space*6),self.y),((xstart + gstt.space*6 + self.ssize),self.y)],self.scolors[6]],
		[[((xstart + gstt.space*7),self.y),((xstart + gstt.space*7 + self.ssize),self.y)],self.scolors[7]],
		[[((xstart + gstt.space*8),self.y),((xstart + gstt.space*8 + bordersize),self.y)],self.scolors[8]],
		]
		
		for pl_color in LOGO:
			c = pl_color[1]
			xy_list = []
			for xy in pl_color[0]:
				xy_list.append((HARP_OFFSET + vectors.Vector2D(xy[0],xy[1])).ToTuple())
			f.PolyLineOneColor(xy_list, c)
