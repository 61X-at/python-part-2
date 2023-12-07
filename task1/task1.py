import random
from warrior import Warrior


first = Warrior()
second = Warrior()

while not first.is_dead() and not second.is_dead():
    match random.randint(0, 2):
        case 0:
            second.take_damage(first.get_power())
            print(f"Атаковал первый юнит. У второго юнита осталось {second.get_health()} здоровья")
        case 1:
            first.take_damage(second.get_power())
            print(f"Атаковал второй юнит. У первого юнита осталось {first.get_health()} здоровья")

print(f"Одержал победу {'первый' if second.is_dead() else 'второй'} юнит")