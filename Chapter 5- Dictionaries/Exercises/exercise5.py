pets = []

pet = {
    'animal':'bird',
    'name':'coco',
    'age':'14',
    'eats':'seeds',
}
pets.append(pet)

pet = {
    'animal':'cat',
    'name':'ginger',
    'age':'4',
    'eats':'cat food',
}
pets.append(pet)

for pet in pets:
    print("\nThings I know about " + pet['name'].title() + ":")
    for key, value in pet.items():
        print(key + ":" + str(value))