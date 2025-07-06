# Variables Exercise -->
birth_year = 2008
current_year = 2025

age = current_year - birth_year
# print(age)

first_name = 'muhammad'
middle_name = 'ahmad'
last_name = 'imran'

my_name = f'{first_name} {middle_name} {last_name}'
# print(my_name)

# Invalid variables names
# continue
# 1nation
# record-one
# record^one

# Numbers Exercise -->
length = 92
breath = 48.8

area = length * breath
# print(round(area))

cost_of_one_packet = 1.49
bought = 9
given_to_the_shopkeeper = 20

remaining_amount = given_to_the_shopkeeper - (cost_of_one_packet * bought)
# print(remaining_amount)

length_of_bathroom = 5.5 ** 2
cost_to_replace_tiles = 500 * length_of_bathroom
# print(cost_to_replace_tiles)

number = 17
binary_number = bin(number)
# print(binary_number)

# Strings Exercise -->

street = 11
city = 'Gujranwala'
country = "Pakistan"

address = 'Street' + ' ' + str(street) + ' ' + 'Wapda Town,' + ' ' + city + ', ' + country
address_2 = f'Street {street} \nWapda Town, {city} \n{country}' 

# print(address_2)

str = "Earth revolves around the sun."

# print(str[-4:-1])

fruits = 3
vegetables = 2

str = f"I eat {vegetables} vegies and {fruits} fruits daily."
# print(str)

s = 'maine 200 banana khaye.'

correct_string = s.replace('200 banana', '10 samosa')
# print(correct_string) 

# Python Lists exercise
m_e = {
  'january': 2200,
  'february': 2350,
  'march': 2600,
  "april": 2130,
  "may": 2190,
}

extra_expense = m_e['february'] - m_e['january']
# print('In feb this much money was spent more than january:', extra_expense)

fqe = m_e['january'] + m_e['february'] + m_e['march']
# print('this is the total expense in the first quater:', fqe)

# for month, exp in m_e.items():
#   if exp == 2000:
#     print('Yes, there is a month where my expense is exactly 2000 and that month is:', month)
#     break

m_e['june'] = 1980
# print(m_e)

m_e['april'] = m_e['april'] + 200
# print(m_e['april'])

heroes = ['spider man','thor','hulk','iron man','captain america']

# print(len(heroes))

heroes.append('black panther') 
heroes.pop()

heroes.insert(3, 'black panther') 

heroes[1:3] = ['doctor strange']
# print(dir(heroes))

heroes.sort()
# print(heroes)

# If statements exercise
# 1.
# sugar_input = int(input('Enter your sugar level: '))

# if sugar_input < 80:
#   print('Your sugar level is very low. Eat something.')
# elif sugar_input > 100:
#   print('Your sugar level is very high. stop eating sweets.')
# else: 
#   print('Your sugar level is normal.')

# 2.
india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore","karachi","islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]

# user_input = input('Enter a city name: ')

# if user_input in india:
#   print(f'{user_input} city is in india.')
# elif user_input in pakistan:
#   print(f'{user_input} city is in Pakistan.')
# elif user_input in bangladesh:
#   print(f'{user_input} city is in bangladesh.')
# else:
#   print('sorry we do not know.')

# city1 = input('Enter 1st city name: ')
# city2 = input('Enter 2nd city name: ')

# if (city1 in india and city2 in india) or (city1 in pakistan and city2 in pakistan) or (city1 in bangladesh and city2 in bangladesh):
#   print('Both of these cities are in same country')
# else:
#   print("They don't belong to same country")

# Python for loop exercises

result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]
heads_count = 0
for value in result:
  if value == "heads":
    heads_count += 1

# print(heads_count)

# for i in range(1, 11):
#   if i % 2 != 0:
#     print(i ** 2)

expense_list = {
  'January': 2340,
  'February': 2500, 
  'March': 2100, 
  'April': 3100, 
  'May': 2980,
}

# user_expense_input = int(input("Enter your expense amount: "))

# for key, value in expense_list.items():
#   if user_expense_input == value:
#     print(f'This expense is occured in {key}.')
#     break;
# print(f"You haven't spent this {user_expense_input} in any month")

# for i in range(1, 6):
#   if i < 5:
#     user_input = input('Are you tired? ')

#   if user_input == 'yes' or user_input == "Yes":
#     print("Very bad, you didn't finish your race")
#     break
#   elif i == 5 and (user_input == 'no' or user_input == 'No'):
#     print('Congratulations, you have completed this race.')
#   elif user_input == 'no' or user_input == 'No':
#     continue

# for i in range(1, 6):
#   print('*' * i)

# Python Functions exercise

def calculate_area(base, height):
  a = (1/2) * base * height
  area = int(a)
  print(area)


# calculate_area(4, 6)

def calculate_area(base, height, shape):
  if shape == 'triangle':
    tri_area = (1/2) * base * height
    triangle_area = int(tri_area)
    print(triangle_area)
  elif shape == 'rectangle':
    rec_area = base * height
    rectangle_area = int(rec_area)
    print(rectangle_area)

# calculate_area(4, 6, 'rectangle')

def stars_pattern(n):
 for i in range(1, n + 1):
   print('*' * i)

# stars_pattern(6)

# Python Dict and Tuples Exercises

countries_population = {
  'china': 143,
  'india': 136,
  'usa': 32,
  'pakistan': 24,
}

# user_input = input('Enter: ')

# if user_input == 'print' or user_input == 'Print':

#   for country, population in countries_population.items():
#     print(f'{country} ==> {population}')

# elif user_input == 'add' or user_input == 'Add':

#   country = input('Which country do you want to add? ')
#   if country not in countries_population.keys():
#     population = int(input('Enter its population in crores: '))
#     countries_population[country] = population
#     for country, population in countries_population.items():
#       print(f'{country} ==> {population}')
#   elif country in countries_population.keys():
#     print("The country is already in the dictionary.")

# elif user_input == 'remove' or user_input == "Remove":

#   country_to_remove = input('Which country do you want to remove? ')
#   if country_to_remove in countries_population.keys():
#     countries_population.pop(country_to_remove, '')
#     for country, population in countries_population.items():
#       print(f'{country} ==> {population}')
#   else:
#     print('The country is already not in the dictionary.')

# elif user_input == 'query' or user_input == 'Query':

#   country_search = input('Which country you want to search for? ')
#   if country_search in countries_population.keys():
#     print(f'The population of {country_search} is', countries_population[country_search], 'crores')
#   else: 
#     print('Sorry, we do not have the data for this country.')

# else: 
#   print('Sorry you can only perform print, add, remove or query operation.')



stock_prices = {
  'info': [600,630,620],
  'ril': [1430,1490,1567],
  'mtl': [234,180,160],
}

# print(stock_prices.values())

# user_input = input('Enter the operation you want to perform: ')

# if user_input == 'print' or user_input == 'Print':

#   for name, value in stock_prices.items():
#     average = round((sum(value)) / len(value), 2)
#     print(f'{name} ==> {value} ==> average: {average}')
    
# elif user_input == 'add' or user_input == "Add":

#   stock_ticker = input('Enter the stock you want to add: ')
#   stock_price = int(input('Enter the price of the stock you want to add: '))

#   if stock_ticker in stock_prices.keys():
#     stock_prices[stock_ticker].append(stock_price)
#     for name, value in stock_prices.items():
#       average = round((sum(value)) / len(value), 2)
#       print(f'{name} ==> {value} ==> average: {average}')
#   else:
#     stock_prices[stock_ticker] = [stock_price]
#     # print(stock_prices[stock_ticker])
#     for name, value in stock_prices.items():
#       average = round((sum(value)) / len(value), 2)
#       print(f'{name} ==> {value} ==> average: {average}')

# else:
#   print('You can only perform print or add operation.')


import math 

def calc_circle(radius):
  area = round(math.pi * (radius ** 2), 2)
  circumference = round(2 * math.pi * radius, 2)
  diameter = round(2 * radius, 2)
  return area, circumference, diameter

if __name__ == '__main__':
  r = input('Enter the radius: ')
  rad = float(r)
  area, c, d = calc_circle(rad)
  print(f'The area, circumference and diameter of the circle is {area}, {c} and {d} respectively.')