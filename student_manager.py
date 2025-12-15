import csv  # Import module for CSV file handling
import os   # Import module to work with files (like checking size)


# Function to add a student to the CSV file
def add_student():
    try:

        name = input("enter your name: ")
        age = int(input("enter your age: "))
        marks = int(input("enter your marks: "))
        city = input("enter your current city name: ")

        # Open the CSV file in append mode
        with open("student.csv","a",newline = "") as f:
            fieldnames = ["name","age","marks","city"]
            csv_writer = csv.DictWriter(f,fieldnames = fieldnames)

            # If file is empty, write the header first
            if os.path.getsize("student.csv") == 0:
                csv_writer.writeheader()
            # Write the student data as a new row        
            csv_writer.writerow({"name":name,"age":age,"marks":marks,"city":city})                  
    except ValueError:
        # Handle invalid input (like letters instead of numbers for age or marks)
        print("enter a valid input")


# Function to read all students from the CSV file
def read_student():
    try:
        with open("student.csv","r") as r:
            csv_read = csv.DictReader(r)
            for row in csv_read:
                print(row) # Print each student as a dictionary
    except FileNotFoundError:
        # Handle case where CSV file does not exist
        print("the give file cannot be  found")


# Function to show statistics of students
def show_Statistics():
    try:
        # Check if file is empty and raise custom exception
        if os.path.getsize("student.csv") == 0:
            print("Given file does not contain data")
            return

        # Open the CSV file for reading
        with open("student.csv","r") as f:
            reader = csv.DictReader(f)
            total = 0       # Total number of students
            above_80 = 0    # Count of students with marks > 80
            avg_marks = 0   # sum of all marks
            avg = 0         # to store average of marks

            # Loop through each student
            for student in reader:
                total += 1
                mark = int(student["marks"])   # Convert marks to integer
                avg_marks += mark
                # Calculate average mark
                avg = avg_marks/total
                if  mark > 80:
                    above_80 += 1
        # Print statistics
        print("total no of students:",total)  
        print("count of students who scored above 80 is: ",above_80) 
        print("average marks is: ",avg) 

        # Open the file "studeny.csv" in read mode as file object r
        with open("student.csv","r") as r:

            data = r.read() # Reads the entire file content as a string
            if data == "":  # Checks if the file is empty
                print("given file does not contain data")

     # Exception handling starts here            
    except FileNotFoundError:
        # This block runs if the file does not exist
        print("File not found")

    except ValueError:
        # This block catches invalid data (e.g., marks not being an integer)
        print("Invalid marks data in file")

#show_statics()

try: 
    with open("student.csv") as f:
        pass
except FileNotFoundError:  
    print("File does not exist. Please create student.csv first.")
else:
    while True:
        try:
            print("\n choose 1 to add students \n 2 to read students\n 3 to show statics \n 4 to exit")
            choice = int(input("choose: "))
            if choice == 1:
                add_student()
            elif choice == 2:
                read_student()
            elif choice == 3:
                show_Statistics()
            elif choice == 4:
                break
            else:
                print("enter a valid input")
        except ValueError:
            print("enter a valid value , your input is invalid")
    

