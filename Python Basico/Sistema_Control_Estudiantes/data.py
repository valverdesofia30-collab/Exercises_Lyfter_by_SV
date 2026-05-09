import csv


def export_students_to_csv(students):
    if not students:
        print("No students registered to export.")
        return
    
    with open("students.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Class Group", "Spanish Grade", "English Grade", "Social Studies Grade", "Science Grade", "Average"])
        
        for student in students:
            writer.writerow([student['name'], student['class_group'], student['spanish_grade'], student['english_grade'], student['social_studies_grade'], student['science_grade'], student['average']])
    print("Students exported successfully!")

def import_students_from_csv(students):
    try:
        with open("students.csv", "r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file)
            
            next(reader)
        
            temp_students = []
        
            has_data = False
        
            for row in reader: 
                has_data = True
                
                name, class_group, spanish_grade, english_grade, social_studies_grade, science_grade, average = row
            
                student = {
                    "name": name, 
                    "class_group": class_group,
                    "spanish_grade": float(spanish_grade),
                    "english_grade": float(english_grade),
                    "social_studies_grade": float(social_studies_grade),
                    "science_grade": float(science_grade),
                    "average": float(average)
                }  
                temp_students.append(student)
        
        if not has_data:
            print("File is empty. No students to import.")
            return
        
        students.clear()
        students.extend(temp_students)
        
        print("Students imported successfully!") 
    
    except FileNotFoundError:
        print("No previous file found.")
        