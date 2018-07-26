class Dog:

    # Class_Attribute
    species = 'mammal'

    # Initializer
    def __init__(self,name,age):
        self.name = name
        self.age = age


dog1 = Dog('pop', 10)
dog2 = Dog('bob', 11)
dog3 = Dog('tot', 12)

print('%s is %d years old!' % (dog1.name, dog1.age))
print('%s is %d years old!' % (dog2.name, dog2.age))
print('%s is %d years old!' % (dog3.name, dog3.age))
print()

oldest_dog_age = 0


def get_biggest_number(*args):
        return max(args)


print(get_biggest_number(dog1.age, dog2.age, dog3.age))
print()


class BullDog(Dog):
    def run(self, speed):
        print('%s runs %s' % (self.name, speed))


class RussellTerrier(Dog):
    species = 'not a mammal'

    def fight(self, strength):
        return '%s fights %s' % (self.name, strength)


dog4 = BullDog('nan', 13)
print('%s is a %s' % (dog4.name,dog4.species))
dog4.run('swiftly')
dog5 = RussellTerrier('zoz', 14)
print(dog5.fight('bravely'))
print(dog4.species)
print(dog5.species)
print()





