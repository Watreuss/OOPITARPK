class Salary:
    def __init__ (self, name, salary):
        self.name = name
        self.salary = int(salary)

    def get_info(self):
        print(f"Работник - {self.name}\nСтавка - {self.salary}")

    def salary_full (self, salary):
        return 0
class PartSalary(Salary):
    def __init__ (self, name, salary, hours):
        super().__init__(name, salary)
        self.hours = int(hours)

    def get_info(self):
        print(f"Работник - {self.name}\nСтавка - {self.salary}, время работы - {self.hours}, и Итоговая зарплата - {self.calculated}")

    def calculate(self, salary, hours):
        self.calculated = self.salary * self.hours
class FullSalary(Salary):
    def __init__ (self, name, salary):
        super().__init__(name, salary)

    def get_info(self):
        print(f"Работник - {self.name}\nСтавка - {self.salary}, коэффицент - 1.2, и Итоговая зарплата - {self.calculated}")

    def calculate(self, salary):
        self.calculated = self.salary * 1.2
def sureness():
    name = input("Ваше имя ? : ").title()
    surname = input("Фамилия ? : ").title()
    fname = surname + " " + name
def main():
    while True:
        name = input("Ваше имя ? : ").title()
        surname = input("Фамилия ? : ").title()
        fname = surname + " " + name
        sure0 = input(f"Вы правильно ввели ? : {surname} {name}, (Yes/No) : ").title()
        if sure0 == "Yes":
            command = input("Какой вид работы вы предпочтёте ?\n1 - Почасовая работа\n2 - Полнодневная работа (Коэфф. - 120 %)\nВаш выбор ? : ")
            if command == "1":
                try:
                    salary = int(input("Ваша ставка ? : "))
                    if salary < 21 and salary / 1 :
                        print("Хорошо, мы принимаем вашу ставку.")
                        hours = int(input("Сколько часов вы собираетесь работать ? : "))
                        if hours < 10 and salary / 1 :
                            pSalary = PartSalary(fname, salary, hours)
                            pSalary.calculate(salary, hours)
                            pSalary.get_info()
                        elif hours in range (10, 25):
                            print("Извиняюсь, но время вашей работы превышает максимальное время почасовой работы!\nПереводим в режим полнодневной зарплаты!")
                            csalary = salary * hours
                            fSalary = FullSalary(fname, csalary)
                            fSalary.calculate(csalary)
                            fSalary.get_info()
                        else:
                            print("Лучше иди выспись перед решением о времени работы.")
                    else:
                        print("Мы к сожалению должны отказать вам... :(")
                except ValueError:
                    print("Пожалуйста, вводите целые числа !")
            elif command == "2":
                try:
                    salary = int(input("Ваша ставка ? : "))
                    if salary < 200 and salary / 1 :
                        print("Хорошо, мы принимаем вашу ставку.")
                        fSalary = FullSalary(fname, salary)
                        fSalary.calculate(salary)
                        fSalary.get_info()
                    else:
                        print("Извиняюсь, но мы должны вам отказать... :(")
                except ValueError:
                    print("Пожалуйста, вводите целые числа !")
            else:
                print("Неизвестная команда.")
        elif sure0 == "No":
            sureness()
        else:
            break
main()
# Я на этот код убил 1 час своей жизни. Прекрасно!