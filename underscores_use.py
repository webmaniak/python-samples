"""Trying some stuff with classes and underscore variables."""

from classes.underscores import Car, ElectricCar # pylint: disable=E0401

# ------------------------------
# Trying some stuff with those classes
# ------------------------------

print("------------------------------")
print("Example usage of the Car class:")
print("------------------------------")

# Correct use
my_car = Car()
my_car.toggle_engine()
while my_car.get_distance() < 10:
    my_car.drive_one_km()
print('You drove for ' + str(my_car.get_distance()) + ' km.')

# Discouraged use (works but not recommended y convention (PEP8))
print('Is engine on? Answer: ' + str(my_car._is_engine_on()))

# Doesn't work. Period.
#print('We currently drove for ' + str(my_car.__distance_counter))

print("------------------------------")
print("Example usage of the ElectricCar class:")
print("------------------------------")

# Correct use
my_electric_car = ElectricCar()
my_electric_car.toggle_engine()
while my_electric_car.get_distance() < 10:
    my_electric_car.drive_one_km()
print('You drove for ' + str(my_car.get_distance()) + ' km.')
print('The remaining autonomy is: ' + str(my_electric_car.get_autonomy()) + ' km.')
print('The battery state is: ' + str(my_electric_car.get_battery_status()) + '%')

# Discouraged use (works but not recommended y convention (PEP8))
print(my_electric_car._autonomy)
print('Is engine on? Answer: ' + str(my_car._is_engine_on()))

# Doesn't work. Period.
#print('We currently drove for ' + str(my_electric_car.__distance_counter))