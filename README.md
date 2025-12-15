
# Student Manager

A Python project to manage student records using CSV files.

## Features
- Add student
- Read students
- Show statistics (total students, average marks, marks > 80)
- Handles invalid input, missing files, and empty files

## How to Run
1. Clone the repository
2. Open terminal in the project folder
3. Run: `python student_manager.py`

## Algorithm: Student Manager

1. Start program
2. Check if students.csv exists
3. Display menu:
   a. Add Student
   b. Read Students
   c. Show Statistics
   d. Exit
4. Get user choice
5. If Add Student:
     - Input name, age, marks, city
     - Validate inputs
     - Save to CSV
6. If Read Students:
     - Open CSV and print each student
     - Handle file not found
7. If Show Statistics:
     - Count total students
     - Count students with marks > 80
     - Calculate average marks
     - Handle empty file or invalid data
8. If Exit → end program
9. If invalid input → show message and go back to menu
10. Repeat menu until user exits

## Flowchart

The following flowchart explains the logic of the Student Manager program:

![Student Manager Flowchart](flowchart.png)






