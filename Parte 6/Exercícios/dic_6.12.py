#26/07/2021

users = [
		{'nickname' : 'aeinstein', 'first' : 'albert', 'last' : 'einsten',
		 'location' : 'princeton'
		},
		
		{'nickname' : 'mcurie', 'first' : 'marie', 'last' : 'curie',
		 'location' : 'paris'
		}
]

for user_info in users:
	print("\nUsername: " + user_info['nickname'])
	
	full_name = user_info['first'] + " " + user_info['last']
	location = user_info['location']
	
	print("\tFull name: " + full_name.title())
	print("\tLocation: " + location.title())
