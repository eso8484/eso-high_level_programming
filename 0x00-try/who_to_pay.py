import random
names = input("Enter the names of ur friends: ")
splitted = names.split(" ")
a = random.randint(0, len(splitted)-1)
print(f"{splitted[a]} will wash the plate")

