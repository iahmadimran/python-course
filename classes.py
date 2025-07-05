sports_cars = ['ferrari', 'lamborghini', 'mclaren', 'koenisegg', 'pagani', 'porsche', 'bmw', 'corvette', 'maserati']

class Cars:
  def __init__(self, car_name, car_model):
    self.car = car_name
    self.model = car_model
  
  def sports_car(self):
    if (self.car == 'ferrari' or self.car =='lamborghini' or self.car =='mclaren' or self.car =='koenisegg' or self.car =='pagani' or self.car =='porsche' or self.car =='bmw' or self.car =='corvette' or self.car =='maserati') and self.model > 2020:
      print(f'your car which is {self.car} is very great')
    elif (self.car == 'ferrari' or self.car =='lamborghini' or self.car =='mclaren' or self.car =='koenisegg' or self.car =='pagani' or self.car =='porsche' or self.car =='bmw' or self.car =='corvette' or self.car =='maserati') and self.model < 2020:
      print(f'your car which is {self.car} is very good but you need to level up.')
    else:
      print(f'your car which is {self.car} is average because it cannot beat supercars')
      

my_car = Cars('mehran', 2022)
my_car.sports_car()

my_friends_car = Cars("koenisegg", 2010)
my_friends_car.sports_car()