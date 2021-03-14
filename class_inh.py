class Student:
    
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __str__(self):
        grade_list = []
        for grade_lists in self.grades.values():
            grade_list.extend(grade_lists)
        avg_grade = sum(grade_list) / len(grade_list)
        courses_in_progress = ', '.join(self.courses_in_progress)
        finished_courses = ', '.join(self.finished_courses)
        return f'Имя: {self.name} \n Фамилия: {self.surname} \nСредние оценки за домашние задания: {avg_grade} \nКурсы в процессе изучения: {courses_in_progress} \nЗавершенные курсы: {finished_courses}'

    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.lecture_grades:
                lecturer.lecture_grades[course] += [grade]
            else:
                lecturer.lecture_grades[course] = [grade]
        else:
            return 'Ошибка'

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        Mentor.__init__(self, name, surname)
        self.name = name
        self.surname = surname
        self.lecture_grades = {}
    
    def __str__(self):
        grade_list = []
        for grade_lists in self.lecture_grades.values():
            grade_list.extend(grade_lists)
        avg_grade = sum(grade_list) / len(grade_list)
        return f'Имя: {self.name} \nФамилия: {self.surname} \nСредние оценки за лекции: {avg_grade}'

class Reviewer(Mentor):
    def __init__(self, name, surname):
        Mentor.__init__(self, name, surname)
        self.name = name
        self.surname = surname
    
    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname}'

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
 
cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']
 
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
 
print(best_student.grades)

cool_lecturer = Lecturer('Another', 'Buddy')
cool_lecturer.courses_attached += ['Python']
 
best_student.rate_lecture(cool_lecturer, 'Python', 9.9)
best_student.rate_lecture(cool_lecturer, 'Python', 9.9)
best_student.rate_lecture(cool_lecturer, 'Python', 9.9)

print(cool_lecturer.lecture_grades)
print(best_student)