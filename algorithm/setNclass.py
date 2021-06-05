class Student :
    __private="i'm still alive!"
    def __init__(self, id, name):
        self.id=id
        self.name=name
    def __repr__(self):
        return f"{self.id} : {self.name}"
        
    def __hash__(self):
        return hash((self.id, self.name))

    def __eq__(self, k):
        return self.id == k.id and self.name == k.name
    def __pr(self):
        print("i'm alive~~")


stu_list=[Student(1,"john"), Student(1,"john"), Student(3,"kane")]
class_ojb_A = Student(1,"john")
# class_ojb_A.private
print(class_ojb_A._Student__private)
# class_obj_B = Student(1,"john")
# # print(class_ojb_A==class_obj_B)
# print(set(stu_list))

#student_list=[('json', 3.5, 201500), ('son', 4.5, 2015001), ('ali', 4.3, 2015002)]
#print(sorted(student_list, key=lambda student: student[2], reverse=True))