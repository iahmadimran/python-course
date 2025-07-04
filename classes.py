sports_cars = ['ferrari', 'lamborghini', 'mclaren', 'koenisegg', 'pagani', 'porsche', 'bmw', 'corvette', 'maserati']

class Cars:
  def __init__(self, car_name, car_model):
    self.car = car_name
    self.model = car_model
  
  def sports_car(self):
    for car in sports_cars:
      if car == self.car:
        print(f'your car which is {self.car} is very great')
      else:
        print(f'Your car which is {self.car} is just average because it cannot beat supercars')
    # if sports_cars[self.car] and self.model > 2020:
    # elif sports_cars[self.car] and self.model < 2020:
    # else:

my_car = Cars('lamborghini', 2022)
my_car.sports_car()

my_friends_car = Cars("koenisegg", 2025)
my_friends_car.sports_car()