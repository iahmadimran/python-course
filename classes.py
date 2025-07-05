sports_cars = ['ferrari', 'lamborghini', 'mclaren', 'koenisegg', 'pagani', 'porsche', 'bmw', 'corvette', 'maserati', 'buggati']

class Cars:
  def __init__(self, car_name, car_model):
    self.car = car_name
    self.model = car_model
  
  def sports_car(self):
    if self.car in sports_cars and self.model > 2020:
      print(f'your car which is {self.car} is very great')
    elif self.car in sports_cars and self.model < 2020:
      print(f'your car which is {self.car} is very good but you need to level up.')
    else:
      print(f'your car which is {self.car} is average because it cannot beat supercars')
      

my_car = Cars('porsche', 2022)
my_car.sports_car()

my_friends_car = Cars("buggati", 2024)
my_friends_car.sports_car()