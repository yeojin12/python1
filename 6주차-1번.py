class Student:
    def __init__(self,name,score):
        self.name = name
        self.score = score

    def get_grade(self):
        if self.score >= 90:
            return "A" 
        elif self.score >= 80:
            return "B"
        elif self.score >= 70:
            return "C"
        else:
            return "F"
        
    def print_list1(self):
        print(f"{student.name} : {student.get_grade()}")
        
N = int(input())
list1 = []

for i in range(1, N+1):
    name, score = input().split()
    score = int(score)
    student = Student(name, score)
    list1.append(student)

print()

for student in list1:
    student.print_list1()