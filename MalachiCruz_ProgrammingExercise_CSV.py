import csv

def write_grades_to_csv():
    """
    Prompts the user for student information and writes it to grades.csv.
    """
    try:
        num_students = int(input("Enter the number of students: "))
    except ValueError:
        print("Invalid input. Please enter a valid integer for the number of students.")
        return

    # Define the header row (field names)
    fieldnames = ['First Name', 'Last Name', 'Exam 1', 'Exam 2', 'Exam 3']

    # Open the file in write mode using the with keyword
    # newline='' is important for preventing blank rows in the CSV file
    with open('grades.csv', 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # Write the header row
        writer.writeheader()

        # Loop to get student information
        for i in range(num_students):
            print(f"\nEntering data for student {i + 1}:")
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            
            grades = []
            for j in range(1, 4):
                try:
                    grade = int(input(f"Enter Exam {j} grade: "))
                    grades.append(grade)
                except ValueError:
                    print(f"Invalid grade input for Exam {j}. Please enter an integer.")
                    # In a real application, you might want to handle this more robustly
                    grades.append(0) # Default to 0 on error

            # Write the student's data as a dictionary
            writer.writerow({
                'First Name': first_name,
                'Last Name': last_name,
                'Exam 1': grades[0],
                'Exam 2': grades[1],
                'Exam 3': grades[2]
            })

    print(f"\nSuccessfully wrote {num_students} student records to grades.csv")

if __name__ == "__main__":
    write_grades_to_csv()
