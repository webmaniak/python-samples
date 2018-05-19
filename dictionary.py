print("------------------------------")
print("Dictionaries")
print("------------------------------")

# Display a single dictionary value
bank_balances = {"Alain" : 1000, "John": 750, "Alice" : 880}
print("Bank balance of Alain: " + str(bank_balances['Alain']))

# Adding a new pair
bank_balances["Barry"] = 575
print(bank_balances)

# Removing a pair
del bank_balances["Alice"]
print(bank_balances)

# Loop across all bank balances
for name, balance in bank_balances.items():
    print(name + " has got " + str(balance) + " CHF")

# Loop only on account owners (keys)
for name in bank_balances.keys():
    print(name + " is a valuable customer.")

# Nesting dictionaries
customers = {
    "Alain": {
        "Account": "000-723-889",
        "Balance": 15000
    },
    "Keith": {
        "Account": "001-856-245",
        "Balance": 6530
    },
    "Rachel": {
        "Account": "000-839-777",
        "Balance": 8000
    }
}

print(customers)