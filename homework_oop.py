class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    # Задание №2. Реализуйте метод выставления оценок лекторам у класса Student.
    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    # Задание №3. Метод посчета средней оценки за дз.
    def avarage_score(self):
        val = self.grades.values()
        avarage = sum(sum(val, [])) / len(sum(val, []))
        return avarage

    # Задание №3. Студенты + средняя оценка за дз
    def __str__(self):
        name_surname_grade = f'Имя: {self.name}\nФамилия: {self.surname}' \
                             f"\nСредняя оценка за домашние задания: {round(self.avarage_score(), 1)}" \
                             f"\nКурсы в процессе изучения:{', '.join(self.courses_in_progress)}" \
                             f"\nЗавершенные курсы:{''.join(self.finished_courses)}"
        return name_surname_grade

    # Задание 3.2. Реализуйте возможность сравнивать (через операторы сравнения) между собой лекторов
    # по средней оценке за лекции и студентов по средней оценке за домашние задания.
    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Сравнение возможно только студента со студентом.')
            return
        return self.avarage_score() < other.avarage_score()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


# Задание №1.
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    # Задание №3. Метод посчета средней оценки за лекции.
    def avarage_score(self):
        val = self.grades.values()
        avarage = sum(sum(val, [])) / len(sum(val, []))
        return avarage

        # Задание №3. Лекторы + средняя оценка за лекции

    def __str__(self):
        name_surname_grade = f'Имя: {self.name}' \
                             f'\nФамилия: {self.surname}' \
                             f'\nСредняя оценка за лекции: {round(self.avarage_score(), 1)}'
        return name_surname_grade

    # Задание 3.2. Реализуйте возможность сравнивать (через операторы сравнения) между собой лекторов
    # по средней оценке за лекции и студентов по средней оценке за домашние задания.
    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Сравнение возможно только лектора с лектором.')
            return
        return self.avarage_score() < other.avarage_score()


# Задание №1.
class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    # Задание №2.
    # В квизе к предыдущей лекции мы реализовали возможность выставлять студентам оценки за домашние задания.
    # Теперь это могут делать только Reviewer (реализуйте такой метод)!
    # Метод, позволяющий выставлять оценки студентам от менторов. Просто перенес из класса Mentor.
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    # Задание №3. Проверяющие
    def __str__(self):
        name_surname = f'Имя: {self.name}\nФамилия: {self.surname}'
        return name_surname


lecturer_1 = Lecturer('Some', 'Buddy')
lecturer_1.courses_attached += ['Python']

lecturer_2 = Lecturer('Herold', 'Wood')
lecturer_2.courses_attached += ['JS']

lecturer_3 = Lecturer('Steave', 'Jobs')
lecturer_3.courses_attached += ['Django']

student_1 = Student('Ruoy', 'Eman', 'male')
student_1.courses_in_progress += ['Python', 'JS', 'Django']
student_1.finished_courses += ['Азбука']
student_1.rate_lecturer(lecturer_1, 'Python', 5)
student_1.rate_lecturer(lecturer_2, 'JS', 7)
student_1.rate_lecturer(lecturer_3, 'Django', 3)

student_2 = Student('Nikola', 'Tesla', 'male')
student_2.courses_in_progress += ['Python', 'JS', 'Django']
student_2.finished_courses += ['Азбука']
student_2.rate_lecturer(lecturer_1, 'Python', 2)
student_2.rate_lecturer(lecturer_2, 'JS', 4)
student_2.rate_lecturer(lecturer_3, 'Django', 9)

reviewer_1 = Reviewer('Donald', 'Trump')
reviewer_1.courses_attached += ['Python']
reviewer_1.rate_hw(student_1, 'Python', 7)
reviewer_1.rate_hw(student_2, 'Python', 3)

reviewer_2 = Reviewer('Albert', 'Enshtein')
reviewer_2.courses_attached += ['JS', 'Django']
reviewer_2.rate_hw(student_1, 'JS', 9)
reviewer_2.rate_hw(student_1, 'Django', 3)
reviewer_2.rate_hw(student_2, 'JS', 8)
reviewer_2.rate_hw(student_2, 'Django', 7.6)

# функция принимает на вход список студентов и название курсов. список студентов создаем сами.
# Помещяем в список экземпляры класса студентов.
# два цикла
# первый перебирает список студентов
# второй перебирает словрик оценок
# потом посчитать среднюю

student_list = [student_1, student_2]

def all_student_score():
    score_py_student = []
    score_js_student = []
    score_dj_student = []
    for student in student_list:
        for subject, score in student.grades.items():
            if subject == 'Python':
                score_py_student.append(score)
            if subject == 'JS':
                score_js_student.append(score)
            if subject == 'Django':
                score_dj_student.append(score)
    middle_py_student = sum(sum(score_py_student, [])) / len(sum(score_py_student, []))
    middle_js_student = sum(sum(score_js_student, [])) / len(sum(score_js_student, []))
    middle_dj_student = sum(sum(score_dj_student, [])) / len(sum(score_dj_student, []))
    return f'Средняя оценка студентов за Python: {middle_py_student} \
      \nСредняя оценка студентов за JS: {middle_js_student} \
      \nСредняя оценка студентов за Django: {middle_dj_student}'


lecturer_list = [lecturer_1, lecturer_2, lecturer_3]

def all_lecturer_score():
    score_py_lecturer = []
    score_js_lecturer = []
    score_dj_lecturer = []
    for lecturer in lecturer_list:
        for subject, score in lecturer.grades.items():
            if subject == 'Python':
                score_py_lecturer.append(score)
            if subject == 'JS':
                score_js_lecturer.append(score)
            if subject == 'Django':
                score_dj_lecturer.append(score)
    middle_py_lecturer = sum(sum(score_py_lecturer, [])) / len(sum(score_py_lecturer, []))
    middle_js_lecturer = sum(sum(score_js_lecturer, [])) / len(sum(score_js_lecturer, []))
    middle_dj_lecturer = sum(sum(score_dj_lecturer, [])) / len(sum(score_dj_lecturer, []))
    return f'Средняя оценка лекторов за Python: {middle_py_lecturer} \
      \nСредняя оценка лекторов за JS: {middle_js_lecturer} \
      \nСредняя оценка лекторов за Django: {middle_dj_lecturer}'

print(student_1)
print(lecturer_1)
print(reviewer_1)
print(all_student_score())
print(all_lecturer_score())

#Готово! Ура-Ура