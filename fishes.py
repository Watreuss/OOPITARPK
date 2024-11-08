import random
class Fish:
    def __init__ (self, name, fish_type, hunger):
        self.name = name
        self.fish_type = int(fish_type)
        self.hunger = int(hunger)

    def swim(self):
        if self.fish_type == 1:
            return f"{self.name} плывет со скоростью 100 М/час"
        elif self.fish_type == 2:
            return f"{self.name} плывет со скоростью 1-2~ Км/час"
        elif self.fish_type == 3:
            return f"{self.name} плывет со скоростью 3-4~ Км/час и умеет делать сальто в воде, йоу!"
        else:
            return f"{self.name} нету в нашем списке."
