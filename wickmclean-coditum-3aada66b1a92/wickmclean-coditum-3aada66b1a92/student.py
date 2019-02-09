# Add any directories, files, or patterns you don't want to be tracked by version control'''
Created on Nov 2, 2018

@author: coditum
'''
class student:
    def __init__(self,student_num, student_name, student_year):
        self.student_num = student_num
        self.student_name = student_name
        self.student_year = student_year
        self.grades = []
#     def __str__(self):
#         return self.student_name
    def addagrade (self, student_grade):
        self.grades.append(student_grade)
s = student(45, 'joe', 2018)
print(s.student_name)
print(s.student_num)

g = student(88, 'sam', 2019)
print(g.student_name)
g.addagrade(81)
print (g.grades)