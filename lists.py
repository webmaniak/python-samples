print("------------------------------")
print("Lists")
print("  They act like a regular array in other languages")
print("------------------------------")

# Creating a list
cars = ["bmw", "mazda", "opel"]
print(cars)

# Updating a list
cars[0] = cars[0].upper()
cars[1] = cars[1].title()
cars[-1] = cars[-1].title()
print(cars)

# Adding something to a list
cars.append("Lomborghini")
print(cars)

# Removing an item from the list
cars.remove("Lomborghini") # also, del cars[3] works when you know the index!
print(cars)

# Add an item at a given index
cars.insert(2, "Ferrari")
print(cars)

# Present a temporarily sorted list
print("This is the original list:")
print(cars)
print("This one is now sorted for display:")
print(sorted(cars))

# Sort alphabeticaly and permanently
print("And now we sort it permanently:")
cars.sort()
print(cars)

# Print the number of elements in the list
print("By the way, the list contains " + str(len(cars)) + " elements.")

print("------------------------------")
print("Loops")
print("------------------------------")

# Loop with list items
position = 1
for car in cars:
    print("Here is the car in position " + str(position) + ": " + car)
    position += 1

# Loop with index
position = 1
for pos in range(len(cars)):
    print("Here's the car at index " + str(pos) + ": " + cars[pos])

# While loop
position = 1
while position < 11:
    print("Index = " + str(position))
    position += 1
print("While loop ended.")

# Slicing a list into a smaller subset
for car in cars[0:2]:
    print(car)

# Copy a list
my_fav_foods = ["spaghetti", "cheese", "chocolate"]
friend_fav_foods = my_fav_foods[:] # /!\ Note the [:] which makes a copy!
first_two_plates = my_fav_foods[:len(my_fav_foods)-1]

print(my_fav_foods)
print(friend_fav_foods)
print(first_two_plates)

friend_fav_foods.insert(1, "avocado")
print(my_fav_foods)
print(friend_fav_foods)

# Loop cars and display BMW in capital letters
for car in cars:
    if car.lower() == 'bmw':
        print(car.upper())
    else:
        print(car.title())

if "Audi" in cars:
    print("You have audi in cars, that's not smart.")
if "Audi" not in cars:
    print("Audi is not a good brand so we won't list it here.")
if "Opel" in cars:
    print("Oh, so you tried Opel already? Good!")