# This python program checks the grade of a student based on their score

# Input is the score of the student
score = int(input("Please input your score \n"))

# Logic is to check the score and print the grade
if score > 90:
    print("Grade is A")
elif score >= 80:
    print("Grade is B")
elif score >= 70:
    print("Grade is C")
elif score >= 60:
    print("Grade is D")
else:
    print("Grade is F")
    