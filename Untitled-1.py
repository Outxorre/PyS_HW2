import random

Lessons = 52 #Это не шутка, в году примерно 52 урока , ориентируясь на шаг если что

class Student:
    def __init__(self, name, age, grades, money):
        self.name = name
        self.age = age
        self.grades = grades
        self.money = money

    def average_grade(self):
        result = int(sum(self.grades) / len(self.grades))
        print("Средний балл:", result)
        return result

    def work(self):
        global Lessons
        Lessons -= 1
        self.money += random.randint(1200, 1800)
        self.grades.append(random.randint(2, 4))
        print(f"{self.name} пошёл на работу. Деньги: {self.money}, Оценки: {self.grades}")

    def learning(self):
        global Lessons
        Lessons -= 1
        self.money -= random.randint(500, 1500)
        self.grades.append(random.randint(6, 10))
        print(f"{self.name} занимается учёбой. Деньги: {self.money}, Оценки: {self.grades}")



student1 = Student("Arlan", 12, [6, 8, 8, 10, 7], 2000)

while Lessons > 0:
    if student1.average_grade()<=4 and student1.money>2000:
        student1.learning()
    elif student1.average_grade()>4 and student1.money<2000:
        student1.work()
    else:
        if random.random() > 0.5:
            student1.work()
        else:
            student1.learning()

if student1.average_grade()>4:
    print("Студент выжил и выпустился!")
elif student1.average_grade()<4:
    print("Отчислен")


