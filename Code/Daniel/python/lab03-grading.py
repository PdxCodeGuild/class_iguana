

def get_grade():
    print("Enter 'x' to quit")
    while True:
        try:
            grade = input("Enter your grade: ")
            if grade == "x":
                break
            else:
                grade = int(grade)

        except ValueError:
            print("Sorry, not a valid grade.")
            continue

        if grade < 0 or grade > 100:
            print("Sorry, that number is outside the grading scale. Please enter another grade:")
        elif grade < 60:
            print("You failed. F")
        elif 70 > grade > 59:
            print("You got a D. Not good enough. Fail")
        elif 80 > grade > 69:
            print("You got a C. Mediocre work my friend")
        elif 90 > grade > 79:
            print("You got a B")
        else:
            print("Congrats, you got an A. Your parents would be proud")



get_grade()