class Teacher:
    height = 180
    money = 200
    happy = 50

class Student(Teacher):
    money = 25
    happy = 10

class Children(Student):
    height = 160


print(Teacher.height)
print(Teacher.money)
print(Teacher.happy)
print(Student.height)
print(Student.money)
print(Student.happy)
print(Children.height)
print(Children.money)
print(Children.happy)
