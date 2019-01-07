"""This file tries to demonstrate how well string concatenation works using different approaches."""

from functions import concat_strings, concat_strings_by_format, concat_strings_by_list, concat_strings_by_map
from classes.timerecorderclass import TimeRecorder

print('------------------------------')
print('Show performances of string concat using 2 args')
print('------------------------------')

print('Test #1: using str1 + str2:')
with TimeRecorder() as t:
    for counter in range(10001):
        concat_strings('Hello', 'World')

print('\nTest #2: using \'{0}{1}\'.format([str1, str2]):')
with TimeRecorder() as t:
    for counter in range(10001):
        concat_strings_by_format('Hello', 'World')

print('\nTest #3: using \'\'.join([str1, str2]):')
with TimeRecorder() as t:
    for counter in range(10001):
        concat_strings_by_list('Hello', 'World')

print('\nTest #4: using \'\'.join(map(str, [str1, str2])):')
with TimeRecorder() as t:
    for counter in range(10001):
        concat_strings_by_map('Hello', 'World')