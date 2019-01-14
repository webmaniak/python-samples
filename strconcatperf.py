"""This file tries to demonstrate how well string concatenation works using different approaches."""

from strings import concat_strings, concat_old_way, concat_new_way, concat_with_lsi, concat_with_str_template, concat_strings_by_list, concat_strings_by_map

from classes.timerecorderclass import TimeRecorder

print('------------------------------')
print('Show performances of string concat using 2 args')
print('------------------------------')

print('Test #1: using str1 + str2:')
with TimeRecorder() as t:
    for counter in range(10001):
        concat_strings('Hello', 'World')

print('\nTest #2: using old way -> \'%1, %2\' % (str1, str2):')
with TimeRecorder() as t:
    for counter in range(10001):
        concat_old_way('Hello', 'World')

print('\nTest #3: using new way -> \'{0}{1}\'.format([str1, str2]):')
with TimeRecorder() as t:
    for counter in range(10001):
        concat_new_way('Hello', 'World')

print('\nTest #4: using the Literal String Interpolation:')
with TimeRecorder() as t:
    for counter in range(10001):
        concat_with_lsi('Hello', 'World')

print('\nTest #5: using string Templates:')
with TimeRecorder() as t:
    for counter in range(10001):
        concat_with_str_template('Hello', 'World')

print('\nTest #6: using list''s \'\'.join([str1, str2]):')
with TimeRecorder() as t:
    for counter in range(10001):
        concat_strings_by_list('Hello', 'World')

print('\nTest #7: using \'\'.join(map(str, [str1, str2])):')
with TimeRecorder() as t:
    for counter in range(10001):
        concat_strings_by_map('Hello', 'World')