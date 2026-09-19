def main():
    done = False
    while not done:
        done = processGradeSet()


def processGradeSet():
    # Read the first grade
    grade1 = input("Enter your 4 grades:\n")
    
    # Handle a sentinel value
    if grade1.upper() == "Q": return True
    
    # Read the next three grades
    gradeToNumber(grade1)
    grade2 = gradeToNumber(input("\n"))
    grade3 = gradeToNumber(input("\n"))
    grade4 = gradeToNumber(input("\n"))
    
    # Compute and print their average
    lowest = min(grade1, grade2, grade3, grade4)
    average = (grade1 + grade2 + grade3 + grade4 -lowest) / 4
    
    return numberToGrade(average)
    

## Converts a letter grade to a number.
# @param grade a letter grade (A+, A, A-, . . ., D-, F)
# @return the equivalent number grade
#
def gradeToNumber(grade):
    if grade == 'A+': return 4.3
    elif grade == 'A': return 4.0
    elif grade == 'A-': return 3.7
    
    elif grade == 'B+': return 3.3
    elif grade == 'B': return 3.0
    elif grade == 'B-': return 2.7
    
    elif grade == 'C+': return 2.3
    elif grade == 'C': return 2.0
    elif grade == 'C-': return 1.7
    
    elif grade == 'D+': return 1.3
    elif grade == 'D': return 1.0
    elif grade == 'D-': return 0.7
    
    elif grade == 'F': return 0.0
    
    else: print("Invalid grade")


## Converts a number to the nearest letter grade.
# @param x a number between 0 and 4.3
# @return the nearest letter grade
#
def numberToGrade(x):
    if x >= 4.15: return "A+"
    elif x >= 3.85: return "A"
    elif x >= 3.5: return "A-"
    
    elif x >= 3.15: return "B+"
    elif x >= 2.85: return "B"
    elif x >= 2.5: return "B-"
    
    elif x >= 2.15: return "C+"
    elif x >= 1.85: return "C"
    elif x >= 1.5: return "C-"
    
    elif x >= 1.15: return "D+"
    elif x >= 0.85: return "D"
    elif x > 0.0: return "D-"
    
    return "F"



main()