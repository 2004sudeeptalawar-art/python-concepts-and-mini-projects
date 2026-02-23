#STUDENT RESULTS SYSTEM
# variales and input
Name = input("Enter your name: ")
Age = int(input("Enter your age: "))

# lists of subjects
subjects = ["Maths", "English", "Science"]

# marks list
marks = []

for subject in subjects:
    mark = int(input(f"Enter your marks for {subject}: "))
    marks.append(mark)

    # operators - Total and Average
    total_marks = sum(marks)
    average_marks = total_marks / len(marks)

# conditional statements - Grade
if average_marks >= 90:
    grade = "A+"
elif average_marks >= 80:
    grade = "A" 
elif average_marks >= 70:
    grade = "B"
elif average_marks >= 60:
    grade = "C"
else:
    grade = "F"
# Dictionary to store studdent results
student_results = {
    "Name": Name,
    "Age": Age,
    "Marks": marks,
    "Total Marks": total_marks,
    "Average Marks": average_marks,
    "Grade": grade
}
# Tuples (grade scale - example use)
grade_scale = (
    ("A+", 90),
    ("A", 80),
    ("B", 70),
    ("C", 60),
    ("F", 0)
)
# Output the results
print("\nStudent Results:")
print("Name:", student_results["Name"])
print("Age:", student_results["Age"])
print("Total Marks:", student_results["Total Marks"])
print("Average Marks:", student_results["Average Marks"])
print("Grade:", student_results["Grade"])