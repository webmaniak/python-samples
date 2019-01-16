"""This file experiments with the NoneType object."""

def try_parse_int(value):
    """Tries to parse the given value into an int."""
    try:
        return int(value)
    except Exception:
        return None

def check_divider(value):
    """Checks whether a divider can be used (formal check style)."""
    if value > 0 or value < 0:
        return value
    else:
        return None

def check_divider_shorter(value):
    """Checks whether a divider can be used (implicit returned value)."""
    if value > 0 or value < 0:
        return value
    else:
        return

def check_divider_shortest(value):
    """Checks whether a divider can be used (implicit return)."""
    if value > 0 or value < 0:
        return value

def check_divider_ternary(value):
    """Checks whether a divider can be used (ternary expression)."""
    return value if value > 0 or value < 0 else None

def greet_only_thomas(name):
    if name and name.lower() == 'thomas':
        print('Hey Thomas, how are you?')
    else:
        print('You\'re not Thomas.')

# ------------------------------
# Experimenting with defined functions
# ------------------------------

# Show that if parse works, a value is returned, otherwise None is returned
result_1 = try_parse_int('7')
result_2 = try_parse_int('6e14')
result_3 = try_parse_int('ABCDE')

print(f'{result_1}, {result_2}, {result_3}')

# Shows how None can be used in tests
greet_only_thomas('Jordan')
greet_only_thomas('Thomas')

# Shows how function syntax can be shortened while keeping the same logic
divider_zero = 0
print(f'Result of formal-style func for value {divider_zero}:'
        f' {check_divider(divider_zero)}')
print(f'Result of shortened func for value {divider_zero}:'
        f' {check_divider_shorter(divider_zero)}')
print(f'Result of implicit func for value {divider_zero}:'
        f' {check_divider_shortest(divider_zero)}')
print(f'Result of ternary func for value {divider_zero}:'
        f' {check_divider_ternary(divider_zero)}')

divider_zero = 5
print(f'Result of formal-style func for value {divider_zero}:'
        f' {check_divider(divider_zero)}')
print(f'Result of shortened func for value {divider_zero}:'
        f' {check_divider_shorter(divider_zero)}')
print(f'Result of implicit func for value {divider_zero}:'
        f' {check_divider_shortest(divider_zero)}')
print(f'Result of ternary func for value {divider_zero}:'
        f' {check_divider_ternary(divider_zero)}')
