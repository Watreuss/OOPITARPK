class club:
    def __init__ (self, name, price):
        self.name = name
        self.price = int(price)

    def get_info(self):
        return f"Имя : {self.name}\nЦена : {self.price}"

    def calc(self):
        return 0

class ClubForHour(club):
    def __init__ (self, name, price, hours):
        super().__init__(name, price)
        self.hours = int(hours)

    def get_info(self):
        return f"Имя : {self.name}\nЦена : {self.price}, и нахождение в клубе на : {self.hours}.\nОкончательная цена : {self.calculated}"

    def calc(self):
        self.calculated = int(calculated)
        self.calculated = self.price * self.hours
        
def main():
    command = input("1 - Почасовая оплата клуба.\n2 - Пакеточная оплата клуба.\nВаш выбор ? : ")
    if command == "1":
        try:
            hours = int(input("Сколько часов ? : "))

        except ValueError:
            print("Вводи числа!")
