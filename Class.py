class MultiFunction():
    Num=int(input("Enter a number:"))
def oddEven():
    if Num %2==1:
        print (Num," is Odd Number")
        Message=Num,"is Odd Number"
    else:
        print(Num,"is Even Number")
        Message=Num,"is Even Number"
        return Message
oddEven()
gender = input("Your Gender: ")
age = int(input("Your Age: "))
def check_marriage_eligibility(gender, age):
    if gender.lower() == "male" and age >= 21:
        return "ELIGIBLE"
    elif gender.lower() == "female" and age >= 18:
        return "ELIGIBLE"
    else:
        return "NOT ELIGIBLE"
eligibility = check_marriage_eligibility(gender, age)
print(eligibility)

        