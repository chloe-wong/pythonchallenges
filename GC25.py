products = {'soda':3,
            'chocolate':5,
            'chips':3,
            'granola':10,
            'water':2}

money = int(input("Please insert your coins into the vending machine"))
print("Here is our selection of products and the corresponding prices.")
for key, value in products.items():
    print(key, value)
choice = str(input("What would you like?"))
price=int((products[choice]))
if price <= money:
    print("your change is:", money-price)
else:
    print("insufficient.")