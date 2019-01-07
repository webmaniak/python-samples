"""This file will do a few things around the number PI"""

filepath = 'data/pi_million_digits.txt'
with open(filepath) as file_obj:
    lines = file_obj.readlines()

pi_string = ''
for line in lines:
    pi_string += line.rstrip()

birthday = input("Please enter your birthday under the form ddmmyy:")
if birthday in pi_string:
    print('The sequence ' + str(birthday) + ' has been found in the first million decimals of PI.')
else:
    print('Bad luck, your sequence is not in the first million decimals of PI...')