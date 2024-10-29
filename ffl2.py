class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = float(salary)  # Преобразуем зарплату в число

    def calculate_salary(self):
        return 0

    def display_info(self):
        return f"Имя сотрудника: {self.name}, зарплата: {self.salary}"


class FullTimeEmployee(Employee):
    def calculate_salary(self):
        self.calculate = self.salary * 1.2
        return self.calculate

    def display_info(self):
        return f"Имя сотрудника: {self.name}, зарплата: {self.salary}\nКоэффициент: 1.2 и окончательная зарплата: {self.calculate}"


class PartTimeEmployee(Employee):
    def __init__(self, name, salary, hours):
        super().__init__(name, salary)
        self.hours = hours

    def calculate_salary(self):
        self.calculate = self.salary * 0.5 * self.hours
        return self.calculate

    def display_info(self):
        return f"Имя сотрудника: {self.name}, зарплата: {self.salary}\nКоэффициент за 1 час работы: 0.5 и окончательная зарплата: {self.calculate}"


def process_salary():
    typeE = input("По часовая зарплата: 1\nДневная зарплата: 2\nВаш выбор?: ")
    name = input("Имя?: ")

    try:
        salary = float(input("Ставка?: "))
        if salary > 1000:
            print("Так делать нельзя! Слишком большая ставка!")
            return
    except ValueError:
        print("Пишите числа!")
        return

    if typeE == "1":
        try:
            hours = float(input("Сколько часов будете работать?: "))
        except ValueError:
            print("Пишите числа!")
            return

        employee = PartTimeEmployee(name, salary, hours)
        employee.calculate_salary()
        print(employee.display_info())
    
    elif typeE == "2":
        employee = FullTimeEmployee(name, salary)
        employee.calculate_salary()
        print(employee.display_info())
    
    else:
        print("Неизвестная команда!")


# Вызов функции для тестирования
process_salary()





