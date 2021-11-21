# dictionaries
sports= {'sport_name':'cricket','matches':'11'}
print(sports['sport_name'])

#adding new key-value pairs
sports['no_of_players']=12
print(sports)

# modifying values in dictionary
sports['matches'] = 12

# looping through dictionary
for key,value in sports.items():
    print(f"\nKey:{key}")
    print(f"Value:{value}")

#remove key-value pairs
del sports['no_of_players']
print(sports)

#nesting dictionaries
sport1= {'sport_name':'cricket','matches':'11'}
sport2= {'sport_name':'hockey','matches':'10'}
sports= [sport1,sport2]
for sport in sports:
    print(sport)




