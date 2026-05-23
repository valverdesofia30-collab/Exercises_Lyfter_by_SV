class Student:
    def __init__(self, name, class_group, spanish_grade, english_grade, social_studies_grade, science_grade):
        self.name = name
        self.class_group = class_group
        self.spanish_grade = spanish_grade
        self.english_grade = english_grade
        self.social_studies_grade = social_studies_grade
        self.science_grade = science_grade
        
    def average_grade(self):
        total = self.spanish_grade + self.english_grade + self.social_studies_grade + self.science_grade
        return total / 4
   