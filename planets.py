planet_list = ["Mercury", "Mars"]

planet_list.append("Jupiter")
planet_list.append("Saturn")

planet_list.extend(["Uranus", "Neptune"])

planet_list.insert(1, "Earth")
planet_list.insert(1, "Venus")

planet_list.append("Pluto")

rocky_planets = planet_list[0:4]

del planet_list[8]

print(planet_list)

spacecraft = [
    ("Pioneer 10", "Jupiter"),
    ("Pioneer 11", "Jupiter"),
    ("Voyager 2", "Jupiter"),
    ("Voyager 1", "Jupiter"),
    ("Galileo", "Jupiter"),
    ("New Horizons", "Jupiter"),
    ("Juno", "Jupiter"),
    ("Pioneer 11", "Saturn"),
    ("Voyager 2", "Saturn"),
    ("Voyager 1", "Saturn"),
    ("Cassini", "Saturn"),
    ("Huygens", "Saturn"),
    ("Voyager 2", "Uranus"),
    ("Voyager 2", "Neptune")
]

for planet in planet_list:
    # iterate over list of tuples
    for tuple in spacecraft:
        if planet in tuple:
    # Print which spacecrafts have visited this planet
            print(f"{tuple[0]} has visited {planet}")