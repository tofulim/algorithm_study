class Student :
    def __init__(self, id, name):
        self.id=id
        self.name=name
    def __repr__(self):
        return f"{self.id} : {self.name}"
        
    def __hash__(self):
        return hash((self.id, self.name))

    def __eq__(self, other):
        return self.id == other.id and self.name == other.name

stu_list=[Student(1,"john"), Student(1,"john"), Student(3,"kane")]
print(set(stu_list))

#student_list=[('json', 3.5, 201500), ('son', 4.5, 2015001), ('ali', 4.3, 2015002)]
#print(sorted(student_list, key=lambda student: student[2], reverse=True))