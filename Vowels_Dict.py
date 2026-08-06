print("Count Vowels Using Dictionary")
n = input("Enter A String: ").lower()
vowels = {
    "a":0,
    "e":0,
    "i":0,
    "o":0,
    "u":0
}
for i in n:
    if i in vowels:
        vowels[i] += 1
print(vowels)