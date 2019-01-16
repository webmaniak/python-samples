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
    """Checks whether the type of the passed value is numeric."""
    return isinstance(value, (int, float, complex))

def try_parse_int(value):
    """Tries to parse the given value into an int."""
    try:
        return int(value)
    except Exception:
        return None

# Checking value types
numeric_one = 1
text_one = '1'
scientific_val = 7.433e-15
float_one = 1.1
none_type = None

print(f'Is {numeric_one} numeric? {is_numeric_value(numeric_one)}!'
        f' It\'s a {type(numeric_one).__name__}')
print(f'Is {text_one} numeric? {is_numeric_value(text_one)}!'
        f' It\'s a {type(text_one).__name__}')
print(f'Is {scientific_val} numeric? {is_numeric_value(scientific_val)}!'
        f' It\'s a {type(scientific_val).__name__}')
print(f'Is {float_one} numeric? {is_numeric_value(float_one)}!'
        f' It\'s a {type(float_one).__name__}')
print(f'Is {none_type} numeric? {is_numeric_value(none_type)}!'
        f' It\'s a {type(none_type).__name__}')

# Testing parse features
print('\n')

print(f'Can {scientific_val} be parsed in an int?')
result = try_parse_int(scientific_val)
if result:
    print('Yes, of course!')
else:
    print('No, unfortunately.')

print(f'Can {text_one} be parsed in an int?')
result = try_parse_int(text_one)
if result:
    print('Yes, of course!')
else:
    print('No, unfortunately.')