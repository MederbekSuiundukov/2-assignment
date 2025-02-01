class Student:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age
class Group:
    def __init__(self, n_group, lst_spisok, professor):
        self.n_group = n_group
        self.lst_spisok = lst_spisok
        self.professor = professor

    def display_group_info(self):
        print(f"Group Name: {self.n_group}")
        print(f"Professor: {self.professor}")
        print("Students in the group:")
        for student in self.lst_spisok:
            print(f"{student.name} {student.surname}, Age: {student.age}")

# Create Student objects
student1 = Student("Marsel", "Sharapov", "18")
student2 = Student("Aibek", "Ubraimov", "19")
student3 = Student("Zhalil", "Kachkynov", "23")
student4 = Student("Kamil", "Tashkulov", "20")
student5 = Student("Bektur", "Abdalimov", "20")
student6 = Student("Akylai", "Dorgoeva", "21")
student7 = Student("Sultanbek", "Muratov", "19")
student8 = Student("Madina", "Kubanychbekova", "20")
student9 = Student("Rinat", "Kubanychbekov", "20")
student10 = Student("Mukadas", "Adylbekova", "20")

students_list = [student1, student2, student3, student4, student5, student6, student7, student8, student9, student10]

group1 = Group(n_group="MATMIE23", lst_spisok=students_list, professor="Dr. Zhenishbek")
group1.display_group_info()

