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
# import random
# foods = ["Pizza", "Burger", "Momos","Biryani","Pasta"]
# choice = random.choice(foods)

# print("Today's Food: ", random.sample(foods,1))


# Rndomly Shuffling A List.
# import random
# n = [1,2,3,4,5]
# random.shuffle(n)
# print(n)


# import datetime
# now = datetime.datetime.now()
# print(now)
# print(now.date())
# print(now.time())
# print(now.year,"-",now.month,"-",now.day)
# print(now.strftime("%d-%m-%Y"))
# print(now.strftime("%H:%M:%S"))
# from datetime import datetime , timedelta
# now = datetime.now()
# future = now + timedelta(days=7)
# print(future)
# past = now - timedelta(days=7)
# print(past)
# Difference In Date 
# date1 = datetime(2026,8,14)
# date2 = datetime(2026,9,1)
# difference = date2 - date1
# print(difference)
# print(difference.days)

# class date.
# from datetime import date
# today = date.today()
# print(today)
# birthday = date(2005,7,18)
# print(today - birthday)




# Class Time.
# from datetime import time , date , datetime
# t = time(14,30,45)
# d = date.today()
# dt = datetime.combine(d,t)
# print(dt)
# print(t)

#OS Module.
import os
current = os.getcwd()
# print(os.listdir())
# print(os.path.exists("prototype.py"))
# print(os.path.isdir("."))
path = os.path.join(current, "prototype.py")
# print(os.path.basename(path)) #gives File Name
# print(os.path.dirname(path))#gives file path
# print(os.path.getsize(path)) #gives File Size in bytes
# print(os.path.splitext(path)) #Split File Text
# print(os.path.getctime(path)) #get file creation time
# print(os.path.getmtime(path)) #it gives file last modified time
# print(os.path.abspath(path)) #it returns Absolute path of the file
# print(os.path.relpath(path)) #it return relative path 
# print(os.path.normpath(path)) #it cleans and normalize the path
path1 = os.path.join(current,"Modules.py")
# print(os.path.commonpath([path,path1])) #returns common path untill change.
# print(os.path.commonprefix([path,path1])) #Returns Common Starting Path
# print(os.path.isabs(path)) #it checks whether the path is absolute
# print(os.path.islink(path)) #it checks whether the path is symbolic linked or not
# print(os.path.isfile(path)) #it checks whether the given file is actual file or not
# print(os.path.isdir(path)) #it checks whether the file is dir/folder or not
# os.mkdir("day43_test") # Creates a Folder on The given Path
# os.rmdir("day43_test") #Deletes the Folder.









