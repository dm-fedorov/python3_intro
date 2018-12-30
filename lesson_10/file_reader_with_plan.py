# file_reader_with_plan.py
try:
    with open('plan.txt', 'r') as file:
        planets = file.readlines()

    print(planets)

    for planet in reversed(planets):
        print(planet.strip())

except Exception as e:
    print(e)
