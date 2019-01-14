"""This file shows the few different ways to concat a string in Python."""

"""
Generally speaking, the rule of thumb should be:
1) If your string is user-defined, use the String Template method (safe)
2) If you use Python 3.6+, use the Literal String Interpolation
3) Otherwise, use the 'new way' method
"""

from string import Template

def concat_strings(str1, str2=''):
    """Concatenates two strings together, the easy way."""
    if str2:
        return str1 + str2
    else:
        return str1

def concat_old_way(str1, str2):
    """Demonstrates the old-fashioned way to concat two strings."""
    return '%s, %s' % (str1, str2)

def concat_new_way(str1, str2):
    """Demonstrates the new way to concat two strings."""
    return '{first}, {second}'.format(first=str1, second=str2)

def concat_with_lsi(str1, str2):
    """Demonstrates a string concat using Literal String Interpolation."""
    """Note: works only from Python 3.6 and upper."""
    return f'{str1}, {str2}'

def concat_with_str_template(str1, str2):
    return Template('$first, $second').substitute(first = str1, second = str2)

"""
Here are a few examples of string concatenators using other objects.
- concat_strings_by_list: uses list.join to concat strings
- concat_strings_by_map: uses the map mechanism to concat strings
"""

def concat_strings_by_list(str1, str2=''):
    """Concatenates two strings using lists."""
    if str2:
        return ''.join([str1, str2])
    else:
        return str1

def concat_strings_by_map(str1, str2=''):
    """Concatenates two strings using maps."""
    if str2:
        result = map(str, [str1, str2])
        return ''.join(result)
    else:
        return str1

def execute_demo():
    test1 = 'Hello'
    test2 = 'Bonjour'
    print(concat_old_way(test1, test2))
    print(concat_new_way(test1, test2))
    print(concat_with_lsi(test1, test2))
    print(concat_with_str_template(test1, test2))
    print(concat_strings_by_list(test1, test2))
    print(concat_strings_by_map(test1, test2))

#execute_demo()