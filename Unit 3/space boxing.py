weight = float(input("What is your weight on Earth? "))
planet = int(input("Which planet do you want to fight on? "))

if planet == 1:
    print("Your weight on Venus is", weight * 0.78)
elif planet == 2:
    print("Your weight on Mars is", weight * 0.39)
elif planet == 3:
    print("Your weight on Jupiter is", weight * 2.65)
elif planet == 4:
    print("Your weight on Saturn is", weight * 1.17)
elif planet == 5:
    print("Your weight on Uranus is", weight * 1.05)
elif planet == 6:
    print("Your weight on Neptune is", weight * 1.23)
else:
    print("Invalid planet.")