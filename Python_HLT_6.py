grade = int(input("Enter your grade number: "))

if grade >= 90:
    print("Grade A*")
if grade >= 80 and grade <= 89:
    print("Grade A")
if grade >= 70 and grade <= 79:
    print("Grade B")
if grade >= 60 and grade <= 69:
    print("Grade C")
if grade <= 59:
    print("Have another go!")