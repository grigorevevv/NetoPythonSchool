class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def grading_lecture(self, lectur, course, grade):
        if isinstance(lectur, Lecturer) and course in self.courses_in_progress and course in lectur.courses_attached:
            if course in lectur.grades:
                lectur.grades[course] += [grade]
            else:
                lectur.grades[course] = [grade]
        else:
            return 'Ошибка'

    def rezult_courses_in_progress(self):
        rezult = ', '.join(str(x) for x in self.courses_in_progress)
        return rezult

    def rezult_finished_courses(self):
        rezult = ', '.join(str(x) for x in self.finished_courses)
        return rezult

    def __str__(self):
        rezult = f'Имя: {self.name} \nФамилия: {self.surname} \
        \nСреднея оценка за домашнее задание: {Lecturer.avg_grades(self)} \
        \nКурсы в процессе изучения: {self.rezult_courses_in_progress()} \
        \nЗавершенные курсы: {self.rezult_finished_courses()}'
        return rezult

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Not a Student')
            return
        return Lecturer.avg_grades(self) < Lecturer.avg_grades(other)


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def avg_grades(self):
        sum_grades = 0
        count_grades = 0
        for course, grade_list in self.grades.items():
            for grade_number in grade_list:
                sum_grades += grade_number
                count_grades += 1
        avg_grad = sum_grades / count_grades
        return avg_grad

    def __str__(self):
        rezult = f'Имя: {self.name} \nФамилия: {self.surname} \nСреднея оценка за лекции: {self.avg_grades()}'
        return rezult

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Not a Lecturer')
            return
        return self.avg_grades() < other.avg_grades()


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        rezult = f'Имя: {self.name} \nФамилия: {self.surname}'
        return rezult


Ruoy_Eman = Student('Ruoy', 'Eman', 'your_gender')
Ruoy_Eman.courses_in_progress += ['Python']
Ruoy_Eman.courses_in_progress += ['GIT']
Ruoy_Eman.finished_courses = ['basics python']

Alex_Fridman = Student('Alex', 'Fridman', 'your_gender')
Alex_Fridman.courses_in_progress += ['Python']
Alex_Fridman.courses_in_progress += ['GIT']
Alex_Fridman.finished_courses = ['basics python']

Elene_Bon = Student('Elene', 'Bon', 'your_gender')
Elene_Bon.courses_in_progress += ['GIT']
Elene_Bon.finished_courses = ['basics python']


reviewer_gates = Reviewer('Bill', 'Gates')
reviewer_gates.courses_attached += ['Python']
reviewer_gates.courses_attached += ['GIT']

reviewer_stark = Reviewer('Tony', 'Stark')
reviewer_stark.courses_attached += ['Python']


lector_smith = Lecturer('Leo','Smith')
lector_smith.courses_attached += ['Python']

lector_gates = Lecturer('Bill', 'Gates')
lector_gates.courses_attached += ['GIT']

Ruoy_Eman.grading_lecture(lector_smith,'Python',7)
Alex_Fridman.grading_lecture(lector_smith,'Python',10)

Ruoy_Eman.grading_lecture(lector_gates,'GIT',9)
Alex_Fridman.grading_lecture(lector_gates,'GIT',8)
Elene_Bon.grading_lecture(lector_gates,'GIT',10)

reviewer_gates.rate_hw(Ruoy_Eman, 'Python', 8)
reviewer_gates.rate_hw(Ruoy_Eman, 'Python', 9)
reviewer_stark.rate_hw(Ruoy_Eman, 'Python', 6)
reviewer_stark.rate_hw(Ruoy_Eman, 'Python', 5)

reviewer_gates.rate_hw(Alex_Fridman, 'Python', 3)
reviewer_gates.rate_hw(Alex_Fridman, 'Python', 5)
reviewer_stark.rate_hw(Alex_Fridman, 'Python', 6)
reviewer_stark.rate_hw(Alex_Fridman, 'Python', 6)

reviewer_gates.rate_hw(Ruoy_Eman, 'GIT',8)
reviewer_gates.rate_hw(Ruoy_Eman, 'GIT',10)
reviewer_gates.rate_hw(Ruoy_Eman, 'GIT',10)

reviewer_gates.rate_hw(Alex_Fridman, 'GIT',5)
reviewer_gates.rate_hw(Alex_Fridman, 'GIT',8)
reviewer_gates.rate_hw(Alex_Fridman, 'GIT',9)

reviewer_gates.rate_hw(Elene_Bon, 'GIT',9)
reviewer_gates.rate_hw(Elene_Bon, 'GIT',10)
reviewer_gates.rate_hw(Elene_Bon, 'GIT',8)


print('Имя студента -', Ruoy_Eman.name)
print('Фамилия студента -', Ruoy_Eman.surname)
print('Оценки студента -', Ruoy_Eman.grades)
print('Курсы студента -', Ruoy_Eman.courses_in_progress)
print('Законченный курсы студента -', Ruoy_Eman.finished_courses)
print()
print()
print('Имя студетна -', Alex_Fridman.name)
print('Фамилия студетна -', Alex_Fridman.surname)
print('Оценки студетна -', Alex_Fridman.grades)
print('Курсы студетна -', Alex_Fridman.courses_in_progress)
print('Законченный курсы студетна -', Alex_Fridman.finished_courses)
print()
print()
print('Имя студетна -', Elene_Bon.name)
print('Фамилия студетна -', Elene_Bon.surname)
print('Оценки студетна -', Elene_Bon.grades)
print('Курсы студетна -', Elene_Bon.courses_in_progress)
print('Законченный курсы студетна -', Elene_Bon.finished_courses)
print()
print()
print('Имя лектора -', lector_smith.name)
print('Фамилия лектора -', lector_smith.surname)
print('Оценки лектора -', lector_smith.grades)
print()
print()
print('Имя лектора -', lector_gates.name)
print('Фамилия лектора -', lector_gates.surname)
print('Оценки лектора -', lector_gates.grades)
print()
print()
print('Имя проверяющего-', reviewer_gates.name)
print('Фамилия проверяющего -', reviewer_gates.surname)
print()
print()
print('Имя проверяющего-', reviewer_stark.name)
print('Фамилия проверяющего -', reviewer_stark.surname)
print()
print()
print(reviewer_gates)
print()
print(reviewer_stark)
print()
print()
print(lector_smith)
print()
print(lector_gates)
print()
print()
print(Elene_Bon)
print()
print(Alex_Fridman)
print()
print(Ruoy_Eman)
print()
print()
print(lector_smith < lector_gates)
print(Elene_Bon < Alex_Fridman)
print(Alex_Fridman < Ruoy_Eman)
print(Ruoy_Eman < Elene_Bon)


def avg_grade_of_student(list,cours):
    sum_grade = 0
    count_grade = 0
    for student in list:
        for cours_in,grade in student.grades.items():
            if cours_in == cours:
                for number in grade:
                    sum_grade += number
                    count_grade += 1
    return round(sum_grade/count_grade,1)

student_list = [Elene_Bon, Alex_Fridman, Ruoy_Eman]
courses = 'Python'

print(avg_grade_of_student(student_list, courses))
print()
print(Elene_Bon.grades) # для проверки
print(Alex_Fridman.grades) # для проверки
print(Ruoy_Eman.grades) # для проверки
print()
print()

def avg_grade_of_lector(list,cours):
    sum_grade = 0
    count_grade = 0
    for lectore in list:
        for cours_in,grade in lectore.grades.items():
            if cours_in == cours:
                for number in grade:
                    sum_grade += number
                    count_grade += 1
    return round(sum_grade/count_grade,1)

lectore_list = [lector_smith,lector_gates]
courses = 'GIT'

print(avg_grade_of_lector(lectore_list, courses))
print()
print(lector_smith.grades) # для проверки
print(lector_gates.grades) # для проверки

