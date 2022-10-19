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
        avarage = sum(val) / len(val)
        return avarage

    # Задание №3. Студенты + средняя оценка за дз
    def __str__(self):
        name_surname_grade = f'Имя: {self.name}\nФамилия: {self.surname}' \
                             f"\nСредняя оценка за домашние задания: {self.avarage_score}" \
                             f"\nКурсы в процессе изучения:{''.join(self.courses_in_progress)}" \
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
        values = self.grades.values()
        avarage = sum(values) / len(values)
        return avarage

        # Задание №3. Лекторы + средняя оценка за лекции
    def __str__(self):
        name_surname_grade = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.avarage_score}'
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

best_student = Student('Ruoy', 'Eman', 'male')
best_student.grades = {'Python': 10, 'JS': 5, 'Swift': 6}
best_student.courses_in_progress = ['Python']

best_student.add_courses('Django')
print(best_student.finished_courses)

non_best_student = Student('Harry', 'Jhonson', 'male')
non_best_student.grades = {'Python': 3, 'JS': 4, 'Swift': 2}
non_best_student.courses_in_progress = ['JS']

non_best_student.add_courses('Git')
print(non_best_student.finished_courses)

lector_1 = Lecturer('Eugeni', 'Borisov')
lector_1.courses_attached = ['Python']

lector_2 = Lecturer('Vitaly', 'Morozov')
lector_2.courses_attached = ['JS']

best_student.rate_lecturer(lector_1, 'Python', 7)
print(lector_1.grades)

non_best_student.rate_lecturer(lector_2, 'JS', 4)
print(lector_2.grades)

print(best_student < non_best_student)

print(best_student)
#print(lector_2)

#print(lector_1 < lector_2)

reviewer_1 = Reviewer('Ivan', 'Belov')
reviewer_1.courses_attached = ['Python']

reviewer_2 = Reviewer('Kirill', 'Ivanov')
reviewer_2.courses_attached = ['JS']

#reviewer_1.rate_hw(best_student, 'Python', 9)
#print(reviewer_1.rate_hw)






#best_student.courses_in_progress += ['Python']
#cool_mentor = Mentor('Some', 'Buddy')
#cool_mentor.courses_attached += ['Python']


