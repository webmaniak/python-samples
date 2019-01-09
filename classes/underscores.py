"""This file demonstrates how underscores can be used in Python."""

class Car():
    """A simplistic representation of a Car."""

    def __init__(self):
        self.brand = 'BMW'
        self.model = 'M4'
        self._autonomy = 500 # in km

        # We don't want the engine state to be accessed from outside
        self._is_powered_on = False

        # We don't want the distance counter to be overriden by a subclass
        self.__distance_counter = 0

    def toggle_engine(self):
        self._is_powered_on = not self._is_powered_on

    def _is_engine_on(self):
        return self._is_powered_on

    def get_distance(self):
        return self.__distance_counter

    def increment_distance(self, increment):
        self.__distance_counter += increment

    def get_autonomy(self):
        return self._autonomy

    def drive_one_km(self):
        if self._is_engine_on():
            if self._autonomy >= 1:
                self._autonomy -= 1
                self.__distance_counter += 1
                print('VROOM!')
            else:
                print('That\'s as far as you can go, buddy')
        else:
            print('The engine is not started, not going anywhere!')


class ElectricCar(Car):
    """A simplistic representation of an electricity-powered Car."""

    def __init__(self):
        super().__init__()
        self._autonomy = 100 # in km
        self._battery_pct = 100 # in percent

        # Will not work:
        self.__distance_counter = 1 # works, but doesn't replace Car's variable

    def get_battery_status(self):
        return self._battery_pct

    def drive_one_km(self):
        if self._is_engine_on():
            if self._autonomy >= 1:
                self._autonomy -= 1
                self._battery_pct -= 1
                self.increment_distance(1)
                print('VROOM!')
            else:
                print('That\'s as far as you can go, buddy')
        else:
            print('The engine is not started, not going anywhere!')
