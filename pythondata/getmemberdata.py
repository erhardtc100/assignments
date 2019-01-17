#Colin and Dana
import json
import csv
from pprint import pprint

#Read superheroes.json

with open('superheroes.json', 'r') as f:
	squad = json.load(f)

#Write a header to the CSV file	
with open('members.csv', 'w') as f:
	writer = csv.writer(f)
	# Write Header
	writer.writerow(['name','age','secretIdentity', 'powers', 'squadName', 'homeTown','formed','secretBase','active'])
	
	#Loop over the members, and for each member write a row to the csv file
	members = squad['members']
	for member in members:
			name = member['name']
			age = member ['age']
			secretIdentity = member['secretIdentity'] 
			powers = member['powers']
			squadName = squad['squadName'] 
			homeTown = squad['homeTown']
			formed = squad['formed']
			secretBase = squad['secretBase']
			active = squad['active']
			writer.writerow([name,age,secretIdentity,powers,squadName,homeTown,formed,secretBase,active])
		
