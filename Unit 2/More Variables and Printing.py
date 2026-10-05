store = "No Frills"
item = "Apples"
price = 0.5
quantity = 7
subtotal = price * quantity
tax = subtotal * 0.05
total = tax + subtotal

print(f"At {store} I bought some {item}.") # F string format
print("They sold for $" + str(price) + " each.") # 
print("I wanted to purchase {} of them.".format(quantity)) #.format method
print(f"The total price, with tax included, was ${round(total, 2)}.") # was missing the f at the beginning of the print
print("The subtotal is {}.".format (round(subtotal, 2)))
print("The tax is {}.".format (round(tax, 2)))
