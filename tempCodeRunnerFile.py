import csv
import os
def add_student():
    try:

        name = input("enter your name: ")
        age = int(input("enter your age: "))
        marks = int(input("enter your marks: "))
        city = input("enter your current city name: ")

        with open("student.csv","a",newline = "") as f:
            fieldnames = ["name","age","marks","city"]
            csv_writer = csv.DictWriter(f,fieldnames = fieldnames)
            if os.path.getsize("student.csv") == 0:
                csv_writer.writeheader()
            csv_writer.writerow({"name":name,"age":age,"marks":marks,"city":city})           
    except ValueError:
        print("enter a valid input")

add_student()
