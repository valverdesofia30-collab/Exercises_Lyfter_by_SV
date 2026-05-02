def add_students(students):
    
    while True:
        name = input("Enter the student full name: ").strip()
        
        if is_valid_name(name):
            break
        else:
            print("Invalid name. It must not be empty or contain numbers. Please try again.")
            
    while True:
        class_group = input("Enter the student class group: ").strip()
        
        if is_valid_section(class_group):
            class_group = class_group.upper()
            break
        else:
            print("Invalid class group. Format should be a number followed by letter (e.g, 5A). Please try again.")
            
    if student_exists(students, name, class_group):
        print("Error: This student already exists in this class group. Please check the name and class group and try again.")
        return
        
    spanish_grade = get_valid_grade("Spanish")
    english_grade = get_valid_grade("English")
    social_studies_grade = get_valid_grade("Social Studies")
    science_grade = get_valid_grade("Science")
    average= (spanish_grade + english_grade + social_studies_grade + science_grade) /4
    
    student = {
        "name": name,
        "class_group": class_group,
        "spanish_grade": spanish_grade,
        "english_grade": english_grade,
        "social_studies_grade": social_studies_grade,
        "science_grade": science_grade,
        "average": average
    }
    students.append(student)
    print("Student added successfully!")


def show_general_average(students):
    if not students:
        print("No students available to calculate the general average.")
        return
    
    total_average = 0
    
    for student in students:
        total_average += student["average"]
        
    general_average = total_average / len(students)
    
    print(f"General average: {general_average}")


def get_valid_grade(subject):
    while True:
        try:
            grade = float(input(f"Enter the student {subject} grade: "))
            if 0 <= grade <= 100:
                return grade
            else:
                print("Invalid grade. Please enter a grade between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a valid grade.")


            
def show_students(students):
    if not students:
        print("No students registered.")
        return
    
    for student in students:
        print(f"Name: {student['name']}, Class Group: {student['class_group']}, Spanish Grade: {student['spanish_grade']}, English Grade: {student['english_grade']}, Social Studies Grade: {student['social_studies_grade']}, Science Grade: {student['science_grade']}")
        
        
def show_top_students (students):
    if not students:
        print("No students registered.")
        return
    
    
    sorted_students = sorted(students, key=lambda student:student["average"], reverse=True)
    top_students = sorted_students[:min(3, len(students))]
    
    if len(students) < 3:
        print("Less than 3 students available, showing all available students.")
    
    for student in top_students:
        print(f"Name: {student['name']}, Class Group: {student['class_group']}, Average Grade: {student['average']}")
        

def delete_student(students):
    if not students:
        print("No students registered.")
        return
    
    name = input("Enter the student full name to delete: ")
    class_group = input("Enter the student class group to delete: ")
    
    for student in students:
        if student["name"].lower() == name.lower() and student["class_group"].lower() == class_group.lower():
            confirm = input(f"Are you sure you want to delete {name} from {class_group}? (yes/no): ")
            
            if confirm.lower() == "yes":
                students.remove(student)
                print("Student deleted successfully!")
            else:
                print("Deletion cancelled.")
            return
        
    print("Student not found. Please check the name and class group and try again.")


def show_failed_students(students):
    if not students:
        print("No students registered.")
        return
    
    failed_student_found = False
    
    for student in students:
        failed_subjects = []
        
        if student["spanish_grade"] < 60:
            failed_subjects.append(("Spanish", student["spanish_grade"]))
        if student["english_grade"] < 60:
            failed_subjects.append(("English", student["english_grade"]))
        if student["social_studies_grade"] < 60:
            failed_subjects.append(("Social Studies", student["social_studies_grade"]))
        if student["science_grade"] < 60:
            failed_subjects.append(("Science", student["science_grade"]))
            
        if failed_subjects:
            failed_students_found = True
            print(f"\nName: {student['name']}")
            print(f"Class Group: {student['class_group']}")
            print("Failed Subjects: ")
            
            for subject, grade in failed_subjects:
                print(f" - {subject}: {grade}")
                
    if not failed_student_found:
        print("No failed students found 🎉.")


def is_valid_name(name):
    if not name.strip():
        return False
    
    for char in name:
        if char.isdigit():
            return False
    return True


def is_valid_section(section):
    if len(section) < 2:
        return False
    
    number_part = section[:-1]
    letter_part = section[-1]
    
    if not number_part.isdigit():
        return False
    if not letter_part.isalpha():
        return False
    
    return True


def student_exists(students, name, class_group):
    for student in students:
        if student["name"].lower() == name.lower() and student["class_group"].lower() == class_group.lower():
            return True
    return False    