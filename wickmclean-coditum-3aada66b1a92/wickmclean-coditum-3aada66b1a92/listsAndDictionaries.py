'''
Created on Nov 2, 2018

@author: coditum
'''
joe_grades = [40, 75, 80, 100]
# print(joe_grades)
# print(joe_grades[2])
print("first loop")
for grade in joe_grades:
    print(grade)
    
print("second loop")
l=len(joe_grades)
for index in range(l):
    print(joe_grades[index])
    
    
print("first dict")
joe_dict = {"hw1":40, "hw2":75, "hw3":80, "hw4":100}
print(joe_dict.items())
print(joe_dict["hw2"])
for key,value in joe_dict.items():
    print(key, value)