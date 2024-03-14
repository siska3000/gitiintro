import requests

from person import Person
from planet import Planet
from starships import Starship


class SWApi:
    def __init__(self):
        self.base_url = "https://swapi.dev/"

    def get_entity(self, entity, entity_id):
        url = f"{self.base_url}/api/{entity}/{entity_id}/"
        responce = requests.get(url)

        if responce.status_code == 200:
            return responce.json()
        else:
            raise ValueError('Imposible to have data')

    def get_person(self, person_id):
        person_dict = self.get_entity('people', person_id)
        return Person(person_dict)

    def get_planet(self, planet_id):
        planet_dict = self.get_entity('planets', planet_id)
        return Planet(planet_dict)

    def get_starhip(self, starship_id):
        starship_dict = self.get_entity('starships', starship_id)
        return Starship(starship_dict)