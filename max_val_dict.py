print("Find The Key With Maximum Value")
n = { 
    "Math" : 95,
    "English": 82,
    "Science": 98,
    "History": 75
}
max_value = -1
max_key = ""
for i,j in n.items():
    if j > max_value:
        max_value = j
        max_key = i
print(max_value ,max_key)