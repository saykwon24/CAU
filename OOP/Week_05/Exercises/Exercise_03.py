# Obtain the number of exam grades per student
exam_num = int(input("How many exam grades does each student have? "))

# Compute average exam grades until the user wants to stop
while True:
    print("Enter the exam grades.")
    total = 0
    # Compute the average grade for one student
    for i in range(1, exam_num + 1):            # range(exam_num)
        grade = int(input("Exam %d: " % i))     # (i + 1)
        total += grade
    
    average = total / exam_num
    print("The average is %.2f" % average)
    
    # Prompt as to whether the user wants to enter grades for another student
    is_N = input("Enter exam grades for another student (Y/N)? ").upper()
    if is_N == 'N':
        break    # break while loop
