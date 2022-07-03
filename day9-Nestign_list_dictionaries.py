travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇

def add_new_country (country, visits, cities):
    new_county = {}
    new_county["country"] = country
    new_county["visits"] = visits
    new_county["cities"] = cities
    travel_log.append(new_county)







#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
add_new_country("Israel", 101, ["Tel aviv", "Haifa", "Givat asaf"])
print(travel_log)



