#Colin and Dana

#Read superheroes.json
import json
from pprint import pprint

with open('superheroes.json', 'r') as f:
    squad = json.load(f)
    
#Creates an empty array called allpowers
allpowers = []

#Loop through members of squad, 
members = squad['members']
for member in members: 
	# append the powers to power array
	powers = member ['powers']
	for power in powers:
        #if power in allpowers: 
		#continue
		#else:
		allpowers.append(power)
#Print those powers to terminal
pprint(allpowers)