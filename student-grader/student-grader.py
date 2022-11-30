def average(file1):
    """
    This function takes in the students.csv file and calculates the average
    """
    for line in file1:
        wordslist = line.split(",")
        sum = 0
        for word in wordslist:
            if word.isdigit():
                num = int(word)
                sum += num
                print("The sum is: ", sum)
            else:
                print("Student name: ", word)

    return sum
def main():
    # Read students from students.csv
    students = []
    with open('./student-grader/students.csv', 'r') as f:
        file1 = f.readlines()
    sum = average(file1)

if __name__ == '__main__':
    main()