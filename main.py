# 1. Піфагорові штани
# Створіть функцію, яка прийматиме масив несортованих чисел і поверне boolean значення залежно від того, чи можна із
# заданих значень скласти піфагорів трикутник з відповідними довжинами сторін.
# Тести:
# [5, 3, 4] -> True
# [6, 8, 10] -> True
# [100, 3, 65] -> False

def pants(container: list) -> bool:
    container.sort()
    return len(container) == 3 and container[0] + container[1] > container[2]


if __name__ == '__main__':
    assert pants([5, 3, 4]) == True
    assert pants([6, 8, 10]) == True
    assert pants([100, 3, 65]) == False


# 2. Рослини проти Зомбі
# Створіть функцію, яка прийматиме два масиви несортованих чисел (перший - масив рослин, що захищається, другий -
# атакуючий масив зомбі) і поверне boolean значення в залежність від того чи перемогли захисники.
# Кожен елемент масиву атакує елемент іншого масиву з тим самим індексом масиву. Той, хто вижив, - це число з найбільшим
# значенням.
# Якщо значення однакове, вони обидва гинуть.
# Якщо одне із значень відсутнє (різна довжина масивів), солдат з непустим значенням виживає.
# Щоб вижити, сторона, що обороняється, повинна мати більше тих, хто вижив, ніж атакуюча сторона.
# У випадку, якщо з обох боків однакова кількість людей, що вижили, перемагає команда з найбільшою початковою силою
# атаки. Якщо загальна сила атаки з обох сторін однакова, поверніть True.
# Початкова сила атаки є сумою всіх значень у кожному масиві.
#
# zombies=[ 1, 3, 5, 7 ] plants=[ 2, 4, 6, 8 ] -> True
# zombies=[ 1, 3, 5, 7 ] plants=[ 2, 4 ] -> False
# zombies=[ 1, 3, 5, 7 ] plants=[ 2, 4, 0, 8 ] -> True
# zombies=[ 2, 1, 1, 1 ] plants=[ 1, 2, 1, 1 ] -> True

def battle(plants: list, zombies: list) -> bool:
    result = []
    zombies_strength = sum(zombies)
    plants_strength = sum(plants)
    zombies_quantity = len(zombies)
    plants_quantity = len(plants)
    if plants_quantity > zombies_quantity:
        plants = plants[:zombies_quantity]
        survived = []
        survived = ['plants'] * (plants_quantity - zombies_quantity)
        result += survived
    elif zombies_quantity > plants_quantity:
        zombies = zombies[:plants_quantity]
        survived = []
        survived = ['zombies'] * (zombies_quantity - plants_quantity)
        result += survived
    for plant, zombie in zip(plants, zombies):
        if plant > zombie:
            result.append('plants')
        elif zombie > plant:
            result.append('zombies')
        else:
            continue
    if result.count('plants') > result.count('zombies'):
        return True
    elif result.count('zombies') > result.count('plants'):
        return False
    else:

        if result.count('plants') == result.count('zombies') and plants_strength < zombies_strength:
            return False
        elif result.count('plants') == result.count('zombies') and plants_strength > zombies_strength:
            return True
        elif result.count('plants') == result.count('zombies') and plants_strength == zombies_strength:
            return True


if __name__ == '__main__':
    assert battle(zombies=[1, 3, 5, 7], plants=[2, 4, 6, 8]) == True
    assert battle(zombies=[1, 3, 5, 7], plants=[2, 4]) == False
    assert battle(zombies=[1, 3, 5, 7], plants=[2, 4, 0, 8]) == True
    assert battle(zombies=[2, 1, 1, 1], plants=[1, 2, 1, 1]) == True

# 3. Генератор розкладу
# Створіть функцію, яка генерує розклад робочих днів працівника.
# Функція приймає кількість днів, на які потрібно скласти розклад, кількість днів роботи, кількість днів відпочинку та
# дату початку розкладу.
# Функція повертає розклад робочих днів співробітника, який генерується починаючи з start_date на days днів уперед,
# враховуючи що співробітник чергує робочі дні (work_days) та дні відпочинку (rest_days).
# Функція має повернути дані у форматі List[datetime.datetime]

# days: 5, work_days: 2, rest_days: 1, start_date: datetime(2020, 1, 30) ->
# [datetime.datetime(2020, 1, 30, 0, 0),
# datetime.datetime(2020, 1, 31, 0, 0),
#   datetime.datetime(2020, 2, 2, 0, 0),
# datetime.datetime(2020, 2, 3, 0, 0)]


from datetime import datetime, timedelta


def generate_schedule(days: int, work_days: int, rest_days: int, start_date: datetime.date) -> list:
    schedule = []
    work_days_var = work_days
    rest_days_var = rest_days
    current_date = start_date
    while len(schedule) < days - rest_days:
        if work_days_var > 0:
            schedule.append(current_date)
            current_date += timedelta(days=1)
            work_days_var -= 1
        if work_days_var == 0:

            rest_days_var -= 1
            current_date += timedelta(days=1)
            if rest_days_var == 0:
                work_days_var = days - work_days - rest_days
                schedule.append(current_date)
                current_date += timedelta(days=1)

    return schedule
