from bs4 import BeautifulSoup

def get_names():
	with open("CC2.html", "r") as fp:
		soup = BeautifulSoup(fp, 'html.parser')
	names = []
	for name in soup.find_all('h3'):
		names.append(name.get_text())
	# print(names)
	counties = []
	for count in soup.find_all('p', 'elegant-profile-panel-description'):
		counties.append(count.get_text())
	print(counties)
	facebooks = []
	for fb in soup.find_all('a', 'fusion-social-network-icon fusion-tooltip fusion-facebook fusion-icon-facebook'):
		facebooks.append(fb.get('href'))
	#print(facebooks)
	#emails = []
	with open("info.txt", "w") as fp:
		while names or counties or facebooks:
			try: 
				n = names.pop()
			except IndexError:
				pass
			try:
				c = counties.pop()
			except IndexError:
				pass
			try:
				f = facebooks.pop()
			except IndexError:
				pass
			fp.write(f"{n}, {c}, {f}\n")


def get_info():
	with open("CC2.html", "r") as fp:
		soup = BeautifulSoup(fp, 'html.parser')
	with open("info2.txt", "w") as fp2:
		# elegant-profile-panel-description-wrapper
		for person in soup.find_all('div', 'fusion-column-wrapper'):
			
			# Name
			#try: 
			name = person.find('h3').get_text()
			# except AttributeError:
			# 	name = ""
			#County
			try: 
				# get('p', 'elegant-profile-panel-description')
				county = person.find('p').get_text()
			except AttributeError:
				county = ""
			# Facebook
			try: 
				fb = person.find('a', 'fusion-social-network-icon fusion-tooltip fusion-facebook fusion-icon-facebook').get('href')
			except AttributeError:
				 fb = ""
				#Website
			try: 
				web = person.find('a', 'fusion-social-network-icon fusion-tooltip fusion-Website fusion-icon-Website').get('href')
			except AttributeError:
				web = ""
			fp2.write(f"{name}, {county}, {fb}, {web}\n" )

if __name__ == "__main__":
	get_info()