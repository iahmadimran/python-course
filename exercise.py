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