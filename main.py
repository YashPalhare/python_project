#Class attendance tracker
from datetime import datetime

def add_student(students):
    name = input("Enter student's name: ")
    roll_no = input("Enter student's roll number: ")

    attendance_data = {
        'daily_attendance': []
    }

    student = {
        'name': name,
        'roll_no': roll_no,
        'attendance_data': attendance_data
    }

    students.append(student)
    print("Student added successfully!\n")

def display_students(students):
    if not students:
        print("No students to display.\n")
        return

    print("Student Details:")
    for student in students:
        attendance_percentage = (sum(student['attendance_data']['daily_attendance']) / len(student['attendance_data']['daily_attendance']) * 100) if student['attendance_data']['daily_attendance'] else 0
        print(f"Name: {student['name']}, Roll No: {student['roll_no']}, Attendance: {attendance_percentage:.2f}%")
    print()

def take_attendance(students):
    if not students:
        print("No students to take attendance for.\n")
        return

    today = datetime.now().strftime("%Y-%m-%d")
    print(f"Taking attendance for {today}...")

    for student in students:
        present = input(f"Is {student['name']} (Roll No: {student['roll_no']}) present? (y/n): ").strip().lower()
        if present == 'y':
            student['attendance_data']['daily_attendance'].append(1)
        else:
            student['attendance_data']['daily_attendance'].append(0)

    print("Attendance recorded successfully!\n")


def main():
    students = []

    while True:
        print("1. Add Student")
        print("2. Display Students")
        print("3. Take Attendance")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_student(students)
        elif choice == '2':
            display_students(students)
        elif choice == '3':
            take_attendance(students)
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.\n")


if __name__ == "__main__":
    main()

