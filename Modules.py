print("Modules")
# import math
# n = int(input("Enter A Number: "))
# print("ceil: ",math.ceil(n))
# print("Square: ",math.pow(n,2))
# print("factorial: ", math.factorial(n))
# print("floor: ", math.floor(n))
# Guessing Number Game.
# import random 
# random = random.randint(1,10)
# i = int(input("Enter Your Guess: "))
# while i != random:
#     if i == random:
#         print("You Guessed The Correct Number!")
#         break
#     else:
#         print("Guess Another Number!")
#     i = int(input("Enter Your Guess: "))
# print("You Guessed The Correct Number! ")

# Random Food Selector.
import random
foods = ["Pizza", "Burger", "Momos","Biryani","Pasta"]
# choice = random.choice(foods)

print("Today's Food: ", random.sample(foods,1))


# Rndomly Shuffling A List.
# import random
# n = [1,2,3,4,5]
# random.shuffle(n)
# print(n)
