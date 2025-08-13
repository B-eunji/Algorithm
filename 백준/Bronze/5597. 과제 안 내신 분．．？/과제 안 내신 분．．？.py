All_students = list(range(1,31))

for i in range(28):
    student = int(input())
    All_students.remove(student)
        
for student in sorted(All_students):
    print(student)
        