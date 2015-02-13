# #!/usr/bin/env python
# flag_color.py
# Olivier Louwaars s2814714
# 13-2-2015

import sys
from random import *
from PyQt4 import QtCore, QtGui

class FlagColor(QtGui.QColor):
	
	def __init__(self):
		super(FlagColor,self).__init__()
		self.randomColor()
	
	def randomColor(self):
		self.setRed(randrange(256))
		self.setBlue(randrange(256))
		self.setGreen(randrange(256))
