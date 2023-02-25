class Robots:


    def __init__(self, model, operate):

        self.__model = model
        self.operate = operate

    # def __str__(self):
    #     return f"Модель корабля: {self.__model}"
    #
    # def walk(self):
    #     print('Ту-ту! Еду в соседнее село!')


class Cleaner(Robots):

    def __init__(self, model, operate, garbage=0):
        super().__init__(model, operate)
        self.model = model
        self.garbage = garbage

    def clean(self):
        self.garbage += 1
        return print(f'Я пылесосю!\nНапылесосил {self.garbage}\n')

class Warbot(Robots):

    def __init__(self, model, operate, gun):
        super().__init__(model, operate)
        self.gun = gun
        self.model = model

    def dry_attack(self):
        return print(f'Робот {self.model} пиздячит по врагам!\n')

class Deep_warrior(Robots):

    def __init__(self, model, operate, gun, deep):
        super().__init__(model, operate)
        self.gun = gun
        self.model = model
        self.deep = deep

    def weat_attack(self):
        return print(f'Подлодка {self.model} бу-лю-лю под водой делает')


clean = Cleaner(124, 'Жужжать')
bot = Warbot('Bum-bum', 'Piu-piu', 'BFG')
seal = Deep_warrior('Imperial', 'Ktulhu', 'tentacles', 1100)
garbage = 0
clean.clean()
bot.dry_attack()
seal.weat_attack()