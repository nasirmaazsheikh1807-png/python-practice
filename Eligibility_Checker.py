print("Eligibility Checker")
class AgeError(Exception):
    pass
try:

    age = int(input("Enter Your Age: "))
    if age<18:
        raise AgeError("Age Must be 18 or above.")

    print("You Are Eligible")
except AgeError as e:
    print("Error",e)