import csv

def read_grades_from_csv():
    """
    Reads the grades.csv file and displays the data in a tabular format.
    """
    try:
        # Open the file in read mode using the with keyword
        with open('grades.csv', 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            
            # Read the header
            header = next(reader)
            print("-" * 50)
            # Use string formatting for a nice tabular look
            print(f"{header[0]:<15} {header[1]:<15} | {header[2]:<6} {header[3]:<6} {header[4]:<6}")
            print("-" * 50)

            # Read and print the rest of the data rows
            for row in reader:
                # Assuming row elements are in the correct order as per the header
                print(f"{row[0]:<15} {row[1]:<15} | {row[2]:<6} {row[3]:<6} {row[4]:<6}")
            print("-" * 50)

    except FileNotFoundError:
        print("Error: grades.csv file not found. Please run the first program to create it.")
    except StopIteration:
        print("Error: grades.csv file is empty or contains only a header.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    read_grades_from_csv()
