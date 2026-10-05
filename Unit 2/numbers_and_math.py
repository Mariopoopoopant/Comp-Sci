print("I have a class of 33 students.") # prints out a statement
print("There are 11 girls, so that means..") # prints out another statement on next line
print("there are " + str(33 - 11) + " boys.") # turns the integer into a string and prints out the value
print() # formatting a space
percentage_girls = round((11/33) * 100, 2) # rounding the girls percentage to 2 decimals
print(f"That means {(percentage_girls)} % are girls...") # prints out a statement saying the percentage
print("and {}% are boys.".format(round((33 - 11) / 33 * 100, 2)))
print()
print("If we made groups of six...")
print(f"There would be {33 // 6} groups of six.")
print(f"And then a smaller group of {33 % 6} people.")
print("-" * 30)
print("If we had 17 apples and 3 people...") # prints out a statement
print(f"Each person would get {17 // 3} whole apples.") # prints out how many apples each person would get without decimals
print("There would be " + str(17 % 3) + " apples remaining.")# prints out the remainder
print() # formatting a space
print("If we charged each person $2 each for their 5 apples..") # prints out a question
print("they would each pay ${}.".format(2 * 5)) # prints out if how much each person pays