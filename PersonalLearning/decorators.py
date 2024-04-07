class Person():

    def __init__(self, firstname, lastname):
        self.first = firstname
        self.last = lastname

    @property
    def fullname(self):
        return self.first + ' ' + self.last

    @fullname.setter
    def fullname(self, name):
        firstname, lastname = name.split()
        self.first = firstname
        self.last = lastname

    @fullname.deleter
    def fullname(self):
        self.first = None
        self.last = None

    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)


# Init a Person
person = Person('Mickey', 'Mouse')
print(person.fullname)
print(person.first)
print(person.last)
print(person.email())

# Setting fullname calls the setter method and updates person.first and person.last
person.fullname = 'Donald Duck'

# Print the changed values of `first` and `last`
print(person.fullname)
print(person.first)
print(person.last)
print(person.email())

# Deleting fullname calls the deleter method, which erases self.first and self.last
del person.fullname

# Print the changed values of `first` and `last`
print(person.first)
print(person.last)
# print(person.fullname)
print(person.email())

person = Person('Goofy', 'Dog')
print(person.fullname)
print(person.first)
print(person.last)
print(person.email())