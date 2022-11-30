def average(student):
    """
    This function takes in a list of grades and returns the average.
    As the list is passed with the student name, we offset the list by 2 to get the grades.
    """
    # Get grades from list
    grades = student[2:]
    total = 0
    # Loop through grades and add them to total
    for grade in grades:
        total += int(grade)
    # Calculate average
    average = total / len(grades)

    # Return average
    return average

def main():
    """
    We first read the students from the file, store them in a list,
    and then loop through the list, calculating the average score for each student.
    """
    # Read students from students.csv
    students = []
    with open('./student-grader/students.csv', 'r') as f:
        for line in f:
            student = line.strip().split(',')
            students.append(student)
    # Loop through students and calculate average
    for student in students:
        print(f'{student[0]} {student[1]} has an average score of {average(student)}')

if __name__ == '__main__':
    main()