# #!/usr/bin/env python
# country.py
# Olivier Louwaars s2814714
# 12-2-2015

class Country:
	
	def __init__(self,country):
		self.country=country


	def __str__(self):
		return "Hello from {}".format(self.country)


def readText():
	countryList=[]
	infile=open("countries_list.txt")
	for line in infile:
		countryList.append(Country(line))
	return countryList



if __name__ == "__main__":
	readText()

