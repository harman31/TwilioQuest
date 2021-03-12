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
