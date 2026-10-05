total_score = 0


print("Are you ready for a quiz?")
print("Okay here it comes!")

print("Q1. What is the capital of Alaska?")
print("     1) Melbourne")
print("     2) Anchorage")
print("     3) Juneau")

answer_1 = int(input(">"))

if answer_1 == 3: 
    print("Correct!")
    total_score + 1
else: 
    print("Incorrect :(")

print("Q2. In python the way you get keyboard input is the keyboard_input function")
print("     1) True")
print("     2) False")

answer_2 = int(input(">"))

if answer_2 == 2:
    print("Correct")
    total_score + 1

else:
    print("Incorrect, the input function is used")

print("Q2. What is the result of 9 + 6 / 3?")
print("     1) 5")
print("     2) 11")
print("     3) 15/3")

answer_3 = int(input(">"))

if answer_3 == 2:
    print("Correct")
    total_score + 1

else:
    print("Incorrect")

print(f"Overall, you got {total_score} out of 3 correct")
print("Thanks for playing")

