class Student:
    def __init__(self, name):
        self.name = name # name of student
        self.courses = {} # key - course, value - grade

    def add_course(self, course_name, grade): # add new course and grade
        self.courses[course_name] = int(grade) # transform string grade to int

    def get_grade(self, course_name): # get student's grade of chosen course
        return self.courses.get(course_name, None)

    def __repr__(self):
        return f"Student(name = {self.name}, courses = {self.courses})"


class CourseManager:
    def __init__(self):
        self.students = {}

    def add_student(self, name, course_name, grade):
        if name not in self.students:
            self.students[name] = Student(name)
        self.students[name].add_course(course_name, grade)

    def get_courses_without_failures(self, passing_scores):
        passing_scores_dict = {
            course: int(score) for course, score in (
                pair.split(',') for pair in passing_scores.split(';')
            )
        }
        all_courses = set(passing_scores_dict.keys())
        courses_with_failures = set()

        for student in self.students.values():
            for course, grade in student.courses.items():
                if grade <= passing_scores_dict[course]:
                    courses_with_failures.add(course)

        courses_without_failures = all_courses - courses_with_failures
        return courses_without_failures


students_info = input().strip()
scores_info = input().strip()

course_manager = CourseManager()
for record in students_info.split(';'):
    name, course_name, grade = record.split(',')
    course_manager.add_student(name, course_name, grade)

courses_without_failures = course_manager.get_courses_without_failures(scores_info)

if courses_without_failures:
    for course in sorted(courses_without_failures):
        print(course)
else:
    print("Пусто")