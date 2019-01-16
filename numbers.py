print("------------------------------")
print("Simple numeric operations")
print("------------------------------")

# Division
print("3 / 2 = " + str(3 / 2))

print("------------------------------")
print("Ranges of numbers")
print("------------------------------")

# Create a list of ints from 1 to 5
one_to_five = list(range(1,6))
print(one_to_five)

# Create a lits of even numbers
even_numbers = list(range(2,12,2))
odd_numbers = list(range(1,10,2))
print(even_numbers)
print(odd_numbers)

some_numbers = [7,3,8,19,44,2]
print(some_numbers)
print("Min: " + str(min(some_numbers)))
print("Max: " + str(max(some_numbers)))
print("Sum: " + str(sum(some_numbers)))

print("------------------------------")
print("Square numbers")
print("------------------------------")

squares = []
for number in range(1,11):
    squares.append(number ** 2)

print(squares)

squares = [value ** 2 for value in range(1,11)]
print(squares)

print("------------------------------")
print("Tests on numbers")
print("------------------------------")

important_ages = [10, 18, 20, 25, 30]
age = 28
if age in important_ages:
    print("Wow, congratulations you are now " + str(age) + "!!!")
elif age == 28:
    print("Hey there, handsome!")
else:
    print("You're not in a special year yet. Don't worry, we'll wait for you.")

print("------------------------------")
print("Exception handling for numbers")
print("------------------------------")

try:
    print(5/0)
except ZeroDivisionError:
    print("Woops! 5 cannot be divided by 0!")

print("------------------------------")
print("Numeric checks")
print("------------------------------")

def is_numeric_value(value):
    return isinstance(value, (int, float, complex))

print(f'Is 1.0 numeric? {is_numeric_value(1.0)}!')
#print(f'Is 1,1 numeric? {is_numeric_value('1,0')}!')
print(f'Is 1 numeric? {is_numeric_value(1.0)}!')
print(f'Is 7e15 numeric? {is_numeric_value(7e15)}!')
#print(f'Is 9spam19 numeric? {is_numeric_value('9spam19')}')