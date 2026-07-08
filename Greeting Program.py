from datetime import datetime
x = datetime.now().hour
if 5 <= x < 12:
    print("Good Morning")
elif 12 <= x < 16:
    print("Good Afternoon")
elif 16 <= x < 20:
    print("Good Evening")
else:
    print("Good Night")