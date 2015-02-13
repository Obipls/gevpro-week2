# #!/usr/bin/env python
# country.py
# Olivier Louwaars s2814714
# 12-2-2015

from flag_color import *

class Country:
	
	def __init__(self,country):
		self.country=country
		
	def countryFlag(self):
		color=FlagColor()
		return color
				

	def __str__(self):
		return "{}".format(self.country)


def readText():
	countryList=[]
	infile=open("countries_list.txt")
	for line in infile:
		countryList.append(Country(line))
	return countryList



		
		
		
	
	

