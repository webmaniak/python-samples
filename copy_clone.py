"""This module shows how copy/clone can be performed in Python."""

import copy

# ------------------------------
# Demonstrate how a shallow copy can be done
# and how you must stay on guard with that
# 
# Note how list_of_list and list_of_list_copy
# show the same items
# ------------------------------

list_of_list = [[1,2,3],[4,5,6],[7,8,9]]
list_of_list_copy = list(list_of_list)

print(f'list_of_list = {list_of_list}')
print(f'list_of_list = {list_of_list_copy}')
print(f'list_of_list == list_of_list_copy ? {list_of_list == list_of_list_copy}')
print(f'list_of_list is list_of_list_copy ? {list_of_list is list_of_list_copy}')
print('------')

list_of_list[0][1] = 20
list_of_list.append([10, 11, 12])
print(f'list_of_list = {list_of_list}')
print(f'list_of_list = {list_of_list_copy}')
print(f'list_of_list == list_of_list_copy ? {list_of_list == list_of_list_copy}')
print(f'list_of_list is list_of_list_copy ? {list_of_list is list_of_list_copy}')
print('------')

# ------------------------------
# Demonstrate how a deep copy can be done
# on a collection of items
# ------------------------------

car_brands = [
                ['Tata', 'Land Rover', 'Jaguar'],
                ['Chevrolet', 'Vauxhall', 'Skoda'],
                ['Toyota', 'Lexus', 'Dahiatsu'],
            ]
car_brands_copy = copy.deepcopy(car_brands)

print(f'car_brands = {car_brands}')
print(f'car_brands_copy = {car_brands_copy}')
print(f'car_brands == car_brands_copy ? {car_brands == car_brands_copy}')
print(f'car_brands is car_brands_copy ? {car_brands is car_brands_copy}')
print('------')

car_brands.append(['MINI', 'BMW', 'Rolls-Royce'])
car_brands[1][2] = 'Skoda!'

print(f'car_brands = {car_brands}')
print(f'car_brands_copy = {car_brands_copy}')
print(f'car_brands == car_brands_copy ? {car_brands == car_brands_copy}')
print(f'car_brands is car_brands_copy ? {car_brands is car_brands_copy}')
print('------')