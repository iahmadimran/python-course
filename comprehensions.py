numbers = [1, 2, 3, 4, 5, 6, 7]
even = [i for i in numbers if i % 2 == 0]
print(even)

countries = ['Pakistan', 'Turkey', 'America']
cities = ['Islamabad', 'Istanbul', 'New York']

z = zip(countries, cities)
geography = {country:city for country,city in z}
print(geography)
