print("------------------------------")
print("User inputs (parrot)")
print("------------------------------")

sentense = input("Tell me something, I'll say it as well: ")
print(sentense)

acknowledge = "nok"
while acknowledge != "ok":
    acknowledge = input("Enter 'ok' to exit the loop: ")
    print("You entered: " + acknowledge)

print("Exited the loop")

# Managing input exceptions (like invalid cast)
first_num = input("Enter a number: ")
second_num = input("Enter a divider: ")
try:
    print(int(first_num) / int(second_num))
except ZeroDivisionError:
    print("You cannot divide " + first_num + " by zero!")
except ValueError:
    pass
    # print("Ah, division of non-numeric values is forbidden!")