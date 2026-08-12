print("Lambda Functions")
from functools import reduce
# try:
n = [1,2,3,4,5] #list(map(int,input("Enter Numbers: ").split())) 
#      m = int(input("Enter Another Number: "))
# except ValueError:  
#     print("Invalid Input! Please Enter a Valid Value.")
cube = lambda a: a**3
sum = lambda a,b: a+b
largest = lambda a,b: a if a>b else b
even_odd = lambda a: "even" if a%2==0 else "odd" #print(even_odd)
#map() + lambda function:
list_square = map(lambda a: a**2 ,n) #print(list(list_square))
even = filter(lambda a: a%2==0 , n) 
factorial = reduce(lambda a,b: a*b , n)#print(factorial)
sort = sorted(n , key = lambda a: a%10 , reverse=True)
even1 = all(i%2==0 for i in n) #any()
names = ["Aman","Rohit","Raj","Karan"]
marks = [85,72,91,68]
result = sorted(zip(names,marks),key=lambda a:a[1])
print(list(result))
