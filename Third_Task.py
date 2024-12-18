class Student:
    def __init__(self, name):
        self.name = name # name of student
        self.courses = {} # key - course, value - grade

    def add_course(self, course_name, grade): # add new course and grade
        self.courses[course_name] = grade

    def get_grade(self, course_name): # get student's grade of chosen course
        return self.courses[course_name]

    def __repr__(self):
        return f"Student(name = {self.name}, courses = {self.courses})"


class CourseManager:
    def __init__(self):
        self.students = {} # тут будут пары Студент : Его балл по предмету
    """Ваш код"""



students_info = input()
a = students_info.split(';')
subjects = [i.split(',') for i in a]
print(subjects)

students = {}
for subject in subjects:
    name, course_name, grade = subject[0], subject[1], subject[2]
    if name not in students:
        students[name] = Student(name=name)
    students[name].add_course(course_name, grade)


# print(students["Анна"].get_grade("Психология"))

def get_grade_for_student(students, student_name, course_name):
    student = students.get(student_name)
    return student.get_grade(course_name)

print(get_grade_for_student(students, "Анна", "Психология"))






# scores_info = input()
#
# splitted_subjects = scores_info.split(';')
# subject_min = [i.split(',') for i in splitted_subjects]
# subject_score = {}
# for i in subject_min:
#     subject_score[i[0]] = int(i[1])
# print(subject_score)

