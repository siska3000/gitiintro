import requests


from star_wars_api import SWApi

r = requests.get("https://swapi.dev/api/people/1/")




api_client = SWApi()
personn = api_client.get_person(1)
print(personn.name)


planets = api_client.get_planet(1)
print(planets.name)

starship = api_client.get_starhip(9)
print(starship.name)