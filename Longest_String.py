print("Return The Longest Word In The String")
n = str(input("Enter a String: "))
longest = ("")
word = ("")
for i in n:
    if i != (" "):
        word += i
        if len(word) > len(longest):
            longest = word
    else:
        word = ("")
        
print(longest)

