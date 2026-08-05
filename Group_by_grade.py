print("Group Students By Grade")
students = {
    "Ali":"A",
    "Rahul":"B",
    "Nasir":"A",
    "Aman":"C",
    "Rohan":"B"
}
sorted = {}
for name,grade in students.items():
    if grade in sorted:
        sorted[grade].append(name)
    else:
        sorted[grade] = []
        sorted[grade].append(name)
print(sorted)