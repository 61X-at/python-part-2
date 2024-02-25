class Student:
    def __init__(self, name_surname: str, group_id: str, grades: list[float]):
        self.grades = grades
        self.group_id = group_id
        self.name_surname = name_surname

    def __str__(self) -> str:
        return f"Студент: {self.name_surname}. Номер группы: {self.group_id}. Оценки: {self.grades}"

    def get_average_grade(self) -> float:
        return sum(self.grades) / len(self.grades)