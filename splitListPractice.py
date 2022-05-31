import random
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(",")

# randomNumber = random.randint(0, len(names)-1)
# finalName = names[randomNumber]

# print(f"{finalName} is gonna pay")

#BETTER WAY
finalName = random.choice(names)
print(f"{finalName} is gonna pay")
