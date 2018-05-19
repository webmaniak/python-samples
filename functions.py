print("------------------------------")
print("Functions")
print("------------------------------")

def greet(name):
    print("Hello, " + name + "!")

def greet_kids(name, isnice = True):
    greet(name)
    if isnice:
        print("You are a nice person.")
    else:
        print("You may need to be more gentle this year...")

def uppercase_first_letter(name):
    return name.title()

def concat_strings(str1, str2=''):
    if str2:
        return str1 + str2
    else:
        return str1

def make_list(*names):
    my_list = []
    for name in names:
        my_list.append(name)
    return my_list

#greet(name='Jeff')

#name = input("Please tell me your name: ")
#greet_kids(uppercase_first_letter(name))

#print(make_list('yellow', 'orange', 'blue'))