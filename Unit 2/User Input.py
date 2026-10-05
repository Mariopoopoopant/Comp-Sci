print("Enter the following information about an item you would like to purchase..")
print()

print("The name of the item:")
name = input()

price = float(input("The price: $"))

print("How many do you want")
quantity = int(input())

subtotal = price * quantity
tax = subtotal * 0.13
total = subtotal + tax

print()
print(f"You choose to buy {quantity} {name}.")
print(f"That will come out to a total ${total}")

