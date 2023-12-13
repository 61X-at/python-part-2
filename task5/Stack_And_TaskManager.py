class TaskManager:
    def __init__(self):
        self.tasks = Stack()

    def new_task(self, name: str, priority: int):
        self.tasks.put(priority, name)

    def delete_task(self, task: tuple[str, int]):
        self.tasks.remove(task[1], task[0])

    def __str__(self) -> str:
        return str(self.tasks)


class Stack:
    def __init__(self):
        self.items: list[tuple[str, int]] = []

    def put(self, priority, item):
        self.items.append((priority, item))
        self.__sort()

    def remove(self, priority, item):
        self.items.remove((priority, item))
        self.__sort()

    def __sort(self):
        self.items.sort(key=lambda task: (task[0], task[1]))

    def __str__(self) -> str:
        return str(self.items)