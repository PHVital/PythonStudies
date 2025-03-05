#--------------- LISTS ---------------
# fruits = ["banana", "orange", "apple", "coconut"]
# fruits.sort(reverse=True)
# print(fruits)

#--------------- TUPLES ---------------
# fruits = ("banana", "orange", "apple", "coconut")
# fruits = tuple(sorted(fruits, reverse=True))
# print(fruits)

#--------------- DICTS ---------------
# fruits = {"banana": 105,
#           "orange": 73,
#           "apple": 72,
#           "coconut": 354}
#  fruits = dict(sorted(fruits.items(), key=lambda item: item[0], reverse=True))
# fruits = dict(sorted(fruits.items(), key=lambda item: item[1]))
# print(fruits)

#--------------- OBJECTS ---------------
class Fruit:
    def __init__ (self, name, calories):
        self.name = name
        self.calories = calories

    def __repr__(self):
        return f"{self.name}: {self.calories}"

fruits = [Fruit("banana", 105),
           Fruit("orange", 73),
           Fruit("apple", 72),
           Fruit("coconut", 354)]

# fruits = sorted(fruits, key=lambda fruit: fruit.name)
fruits = sorted(fruits, key=lambda fruit: fruit.calories)

print(fruits)