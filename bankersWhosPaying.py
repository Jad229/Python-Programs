import random

bankers_string = input("Give me everyones name seperated by a comma ") 

bankers = bankers_string.split(",")

rand_int = random.randint(0, len(bankers) - 1)

print(f"{bankers[rand_int]} is going to buy the meal today!")

