class Rectangle:
   def __init__(self, length, breadth, unit_cost=0):
       self.length = length
       self.breadth = breadth
       self.unit_cost = unit_cost
   def get_area(self):
       return self.length * self.breadth
   def calculate_cost(self):
       area = self.get_area()
       return area * self.unit_cost
# breadth = 120 units, length = 160 units, 1 sq unit cost = Rs 2000
r = Rectangle(160, 120, 2000)
print("Area of Rectangle: %s sq units" % (r.get_area()))

class Data2:
 
    def __init__(self, i, n):
        print('Data2 Constructor')
        self.id = i
        self.name = n
 
 
d2 = Data2(10, 'Secret')
print(f'Data ID is {d2.id} and Name is {d2.name}')

class Citizen:
    """A not-so-simple example Class"""

    def __init__(self, first_name, last_name):
        self.first_name = str(first_name)
        self.last_name= str(last_name)

    def full_name(self):
        return self.first_name + ' ' + self.last_name

    greeting = 'For the glory of Python!'

x = Citizen('No', 'Way')
print(x.full_name())