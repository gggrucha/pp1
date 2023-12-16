'''
29.	The grades.txt file contains student's grades. Create the file in any text editor.
Name: Peter
Grades: 3.5, 4.0, 5.0, 4.5, 3.5, 3.0, 5.0
Then create a program that calculates the arithmetic mean of student's grades.
'''
#chad lgbt 

def calculate_mean(grades):
    total = sum(grades)
    mean = total / len(grades)
    return mean

def read_grades_from_file(file_path):
    with open(file_path, 'r') as file:
        content = file.readlines()
        # Assuming the grades line is the second line in the file
        grades_line = content[1].split(":")[1].strip()
        grades = [float(grade) for grade in grades_line.split(",")]
        return grades

if __name__ == "__main__":
    file_path = r"D:\test\grades.txt"  # Update the file path if needed
    grades = read_grades_from_file(file_path)

    if grades:
        mean = calculate_mean(grades)
        print(f"The arithmetic mean of {file_path} is: {mean}")
    else:
        print("No grades found in the file.")
