import requests

def fetch_planet_data():
    url = "https://api.le-systeme-solaire.net/rest/bodies/"
    response = requests.get(url)
    planets = response.json()['bodies']
    planet_data = []

    for planet in planets:
        if planet['isPlanet']:
            name = planet.get('englishName', 'N/A')
            mass = planet.get('mass', {}).get('massValue', 'N/A')
            orbit_period = planet.get('sideralOrbit', 'N/A')
            planet_data.append((name, mass, orbit_period))

    return planet_data

def find_heaviest_planet(planets):
    heaviest = max(planets, key=lambda x: x[1])
    return heaviest[0], heaviest[1]

if __name__ == "__main__":
    planets = fetch_planet_data()

    for name, mass, orbit_period in planets:
        print(f"Planet: {name}, Mass: {mass}, Orbit Period: {orbit_period} days")

    name, mass = find_heaviest_planet(planets)
    print(f"\nThe heaviest planet is {name} with a mass of {mass} kg.")
