import random
from student import Student

students = [
    Student("Вася Пупкин", "1", [round(random.uniform(2, 5)) for _ in range(5)]),
    Student("Николай Николаев", "1", [round(random.uniform(2, 5)) for _ in range(5)]),
    Student("Петя Форточкин", "2", [round(random.uniform(2, 5)) for _ in range(5)]),
    Student("Надежда Надежная", "2", [round(random.uniform(2, 5)) for _ in range(5)]),
    Student("Валерий Миладзе", "3", [round(random.uniform(2, 5)) for _ in range(5)]),
    Student("Виктор Цой", "3", [round(random.uniform(2, 5)) for _ in range(5)]),
    Student("Ариана Гранде", "4", [round(random.uniform(2, 5)) for _ in range(5)]),
    Student("Ольга Бузова", "4", [round(random.uniform(2, 5)) for _ in range(5)]),
    Student("Давид Петросян", "5", [round(random.uniform(2, 5)) for _ in range(5)]),
    Student("Иосиф Сталин", "5", [round(round(random.uniform(2, 5)), 2) for _ in range(5)]),
]

students = sorted(students, key=lambda student: student.get_average_grade())

print("\n".join(map(str, students)))