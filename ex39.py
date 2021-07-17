states = {"Gujrat" : "Guj",
"Maddhya Paradeh" : "MP",
"Rajsthan" : "Raj"}
cities = {
    'Guj': 'Ahemedabad',
    'MP': 'Rajkot',
    'Jam': 'Jamnagar',
     0 : None,
     'Raj': 'Jaypur'
    }
    
cities['Del'] = 'Delhi'
cities['Pun'] = 'Pune'
print(cities[0])
print(cities['Pun'])
print('#'*10)
good = 'Rajstan' in states
print(good)
print('#'*10)

#printing cities
print('*'*10)
print("Gujarat state has %s city"%cities['Guj'])
print("Rajastan state has %s city"%cities['Jam'])


#printing states

print('#'*10)
print("Gujarat abbreviation is %s "%states['Gujrat'])
print("Madhya pradesh abbreviation is %s "%states['Maddhya Paradeh'])


#printing both
print('-'*20)
print("Gujarat has ", cities[states['Gujrat']])
print("Rajsthan has ", cities[states['Rajsthan']])

#iterating through the dict

print('='*10)

for state, abbrv in states.items():
    print("%s state has %s abbreviation"%(state,abbrv))
    
    
print('-'*10)

for city, abbrv in cities.items():
    print("%s state has %s city"%(city,abbrv))
    
    
# iterating through two dicts
print('\n')
print('*'*20)

for state,abbrv in states.items():
    print("%s state is abbreviate as %s and has city %s"%(state,abbrv,cities[abbrv]))
    
state = states.get('Gujrat')
print(state)

if not state:
    print("sorry no Haryana")
    
city = cities.get('Bhv','So soory it could not found for you')
print('\'Bhv\'',city)

time = {
    '1234': { '0': 'hey how are you'},
    '1453': { '0': 'please get up'}
    }
    
time['1453']['2']= 'get up its moring time'
        
for i, value in time.items():
    if i== '1453':
        print(time['1234']['0'])
        time['1234']['0']
        #list(time.items)
        print(list(time.items())[0][1])

