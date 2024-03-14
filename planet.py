class Planet:
    def __init__(self, data):
        self.name = data["name"]
        self.rotation_period = data["rotation_period"]
        self.orbital_period = data["orbital_period"]
        self.diameter = data["diameter"]
        self.climate = data["climate"]
        self.gravity = data["gravity"]
        self.terrain = data["terrain"]
        self.surface_water = data["surface_water"]
        self.population = data["population"]
        self.residents = data["residents"]
        self.films = data["films"]
        self.created = data["created"]
        self.edited = data["edited"]
        self.url = data["url"]

