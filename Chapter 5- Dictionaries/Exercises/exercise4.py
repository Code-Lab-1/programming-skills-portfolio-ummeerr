rivers = {
    'nile': 'egypt',
    'jhelum':'Pakistan',
    'Congo':'Africa',
    'Amazon riveer':'South America',
    'Yellow river':'China',
}

for river, country in rivers.items():
    print("The " + river.title() +  " flowes through " + country.title() + "." )

print("\nThe rivers are includedin this data set:")
for river in rivers.keys():
    print("-" + river.title())

print("\nThe countries are included in this data set:")
for country in rivers.values():
    print("-" + country.title())