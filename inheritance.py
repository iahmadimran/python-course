class Vehicle:
  def gerneral_usage(self):
    print('general use: transportation')

class Car(Vehicle):
  def __init__(self):
    print("I'm Car.")
    self.wheels = 4
    self.has_roof = True

  def specific_usage(self):
    self.gerneral_usage()
    print('specific usage: commute to work, vacation with family')

class MotorCycle(Vehicle):
  def __init__(self):
    print("I'm MotorCycle.")
    self.wheels = 2
    self.has_roof = False

  def specific_usage(self):
    self.gerneral_usage()
    print('specific usage: road trips, racings, wheeling, shughal mela with friends etc')


# c = Car()
# c.specific_usage()

# m = MotorCycle()
# m.specific_usage()

# print(issubclass(Car, Vehicle))

class Father:
  def skills(self):
    print('gardening, management, watching news')

class Mother:
  def skills(self):
    print('cooking, detective skills, art, sewing')

class Child(Father, Mother):
  def skills(self):
    Father.skills(self)
    Mother.skills(self)
    print('sports, programming, statistics, maths')

c = Child()
c.skills()