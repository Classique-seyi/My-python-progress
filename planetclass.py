class Planet:
    def __init__(self, name, planet_type, star):
        self.name = name
        self.planet_type = planet_type
        self.star = star
        if not isinstance(name, str) or not isinstance(planet_type, str) or not isinstance(star, str):
            raise TypeError('name, planet type, and star must be strings')

        if name == "" or planet_type == "" or star == "":
            raise ValueError("name, planet_type, and star must be non-empty strings")
        pass

    def orbit(self):
        return f"{self.name} is orbiting around {self.star}..."
    
    def __str__(self):
        return f"Planet: {self.name} | Type: {self.planet_type} | Star: {self.star}"


planet_1 = Planet('Precious', 'Earth', 'Tesla')
planet_2 = Planet('Seyi', 'Pluto', 'Sharon')
planet_3 = Planet('Tolu', 'Mars', 'Luke')


print(planet_1.orbit())
print(planet_2.orbit())
print(planet_3.orbit())

print(planet_1.__str__())
print(planet_2.__str__())
print(planet_3.__str__())

print(planet_1)
print(planet_2)
print(planet_3)