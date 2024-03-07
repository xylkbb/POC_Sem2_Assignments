class Dog():
    counter = 0

    def __init__(self, name, age):
        self.__name = name
        self.age = age
        Dog.counter += 1


my_pet = Dog('Teddy', 2)
kates_pet = Dog('Foxy', 5)
adams_pet = Dog('Luna', 1)

print(my_pet.counter)
print(kates_pet.counter)
print(adams_pet.counter)


class Dog():
    __counter = 0

    def __init__(self, name, age):
        self.__name = name
        self.age = age
        Dog.__counter += 1


class Dog():
    counter = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Dog.counter += 1


my_pet = Dog('Tom', 5)

if hasattr(my_pet, 'name'):
    print('My pet is called', my_pet.name)
else:
    print('My pet has no name')

if hasattr(Dog, 'counter'):
    print('The Dog class has a counter!')
else:
    print('The Dog class does not have a counter')


class House():
    counter = 0

    def __init__(self, address, area, price):
        self.address = address
        self.area = area
        self.price = price
        House.counter += 1

        House.quality = 'low'
        self.quality = 'medium'
        quality = 'high'

        print(House.quality, self.quality, quality)

    def present(self):
        print('The house at', self.address, 'has an area of',
              self.area, 'and costs', self.price)


soho_house = House('12 Lexington St, Soho', 130, 540000)
soho_house.present()
print(House.counter)


class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age


