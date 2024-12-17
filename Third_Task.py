# class Student:
#     def __init__(self, name):
#         self.name = name
#         self.courses = {}
#     """Ваш код"""
#
#
# class CourseManager:
#     def __init__(self):
#         self.students = {}
#     """Ваш код"""
#
#
# students_info = input()


scores_info = input()
splitted_subjects = scores_info.split(';')
print(splitted_subjects)

subject_min = [i.split(',') for i in splitted_subjects]
print(subject_min)
subject_score = {}
for i in subject_min:
    subject_score[i[0]] = int(i[1])
print(subject_score)