"""This module shows how copy/clone can be performed in Python."""

# ------------------------------
# Demonstrate how a deep copy can be done
# on a first-level collection
# ------------------------------
fruit_list = ['Banana', 'Orange', 'Mango']
fruit_list_copy = list(fruit_list)

print(f'fruit_list = {fruit_list}')
print(f'fruit_list_copy = {fruit_list_copy}')
print(f'fruit_list == fruit_list_copy ? {fruit_list == fruit_list_copy}')
print(f'fruit_list is fruit_list_copy ? {fruit_list is fruit_list_copy}')
print('------')

fruit_list[1] = 'Pineapple'
print(f'fruit_list = {fruit_list}')
print(f'fruit_list_copy = {fruit_list_copy}')
print(f'fruit_list == fruit_list_copy ? {fruit_list == fruit_list_copy}')
print(f'fruit_list is fruit_list_copy ? {fruit_list is fruit_list_copy}')
print('------')

# ------------------------------
# Demonstrate how a shallow copy can be done
# and how you must stay on guard with that
# ------------------------------

list_of_list = [[1,2,3],[4,5,6],[7,8,9]]
list_of_list_copy = list(list_of_list)

print(f'list_of_list = {list_of_list}')
print(f'list_of_list = {list_of_list_copy}')
print(f'list_of_list == list_of_list_copy ? {list_of_list == list_of_list_copy}')
print(f'list_of_list is list_of_list_copy ? {list_of_list is list_of_list_copy}')
print('------')

list_of_list[0][1] = 20
print(f'list_of_list = {list_of_list}')
print(f'list_of_list = {list_of_list_copy}')
print(f'list_of_list == list_of_list_copy ? {list_of_list == list_of_list_copy}')
print(f'list_of_list is list_of_list_copy ? {list_of_list is list_of_list_copy}')
print('------')