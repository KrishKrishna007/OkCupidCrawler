from pyokc import pyokc
from pprint import pprint

u = pyokc.User()

profile_list = u.search(location= 'Reston', number=100,age_min=26, age_max=32)
for profile in profile_list:
	print("######################")
	print("Name: "+ profile.name)
	print("Age: "+ str(profile.age))
	print("Match: "+ str(profile.match))
	print("Rating: "+ str(profile.rating))

