#attendance tracker

students = {}

def add_student(name):
    students[name] = "Absent"

def mark_present(name):
    if name in students:
        students[name] = "Present"

def show_attendance():
    if not students:
        print("No students added yet.")
    else:
        print("Attendance Status:")
        for name, status in students.items():
            print(f"{name}: {status}")