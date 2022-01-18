from starModel import StarModel #1.
from typing import List   #4.

class Star:
	def __init__(self):
		self.file_name = 'stars.txt' #5.
		self.lines = []
		self.stars: List[StarModel] = []
		self.sepa = '-------------------'
	
	def read_content(self):
		fp = open(self.file_name, 'r')
		self.lines = fp.readlines()
		fp.close #6.
	
	def convert_content(self):
		for line in self.lines[1::]: #7.
			(name, constellation, 
			distance, mass, temperature, age) = line.split(':')
			
			starModel = StarModel(
				name, constellation, 
				float(distance.replace(',','.')),  #8.
				float(mass.replace(',', '.')), 
				int(temperature), 
				float(age.replace(',', '.')))

			self.stars.append(starModel)
	
	def print_out(self):
		for star in self.stars:
			print(star.name, star.constellation)  #9.
	
	# Van-e csillag a Göncöl csillagképben #12.
	def star_in_goncol(self):
		n = len(self.stars)
		i=0
		while i<n and self.stars[i].constellation.find('Göncöl') != -1:	
			i += 1		
		if i<n:
			print('Van')
		else:
			print('Nincs')

	# Legtávolabbi csillag neve, távolsága #13.
	def farthest_star(self):
		max_star = self.stars[0]
		for star in self.stars:
			if star.distance > max_star.distance:
				max_star = star
		print('Legtávolabbi:', max_star.name, max_star.distance)

	# Legalacsonyabb hőmérsékletű csillag #14.
	def lowest_temperature_star(self):
		min_star = self.stars[0]
		for star in self.stars:
			if star.temperature > min_star.temperature:
				max_star = star
		print('Lealacsonyabb:', min_star.temperature)

	# A Csillagok átlagéletkor #15.
	def average_age_of_stars(self):
		osszeg = 0
		for star in self.stars:
			osszeg += star.age 
		darab = len(self.stars)
		atlag = osszeg / darab
		print('Átlag: %.2f' % atlag)
 
	# a Kepler-18 hány kiloggram tömegű #16.
	def weight_of_kepler18(self):
		for star in self.stars:
			if star.name == 'Kepler-18':
				print('A csillag tömege:', star.mass * 1.98892 * (10**30))
			
	# 150 fényévnél közelbbi bolygók neve és távolsága #17.
	def close_stars(self):
		print(self.sepa)
		for star in self.stars:
			if star.distance < 150:
				print("150 fényévnél közelbbi bolygók neve és távolsága: ", star.name, star.distance)
			

	# A Szextánok csillagképben található csillagok adatai #18.
	def szextan_datas(self):
		print(self.sepa)
		for star in self.stars:
			if star.constellation == 'Szextánok':
				print("A Szextánok csillagképben található csillagok adatai: ",star.name, star.constellation, star.distance, star.mass, star.age, star.temperature)

	# A 2 M-nél kisebb tömegű csillagok neve és tömege
	def less_than_two_mass_stars(self):
		print(self.sepa)
		for star in self.stars:
			if star.mass < 2:
				print("A 2 M-nél kisebb tömegű csillagok neve és tömege: ", star.name, star.mass)


star = Star() 
star.read_content()
#star.average_age_of_stars()
star.convert_content()
star.star_in_goncol() 
star.farthest_star() 
star.lowest_temperature_star() 
star.weight_of_kepler18()             # 10.-11.
star.close_stars() 
star.szextan_datas() 
star.less_than_two_mass_stars() 








