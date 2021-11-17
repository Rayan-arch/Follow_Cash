from views.mainMenu import AbstractMenu
from time import sleep
from controllers.controllers import Add, Delete, Statement


class Start(AbstractMenu) :
    def __init__(self) :
        super().__init__()
        self.options = {
            1 : People,
            2 : Income,
            3 : Exit
        }

    def __str__(self) :
        return 'Main Menu'


class People(AbstractMenu) :
    def __init__(self) :
        super().__init__()
        self.options = {
            1 : Add,
            2 : Delete,
            3 : Statement,
            4 : Start
        }

    def __str__(self) :
        return 'People'


class Income(AbstractMenu) :
    def __init__(self) :
        super().__init__()
        self.options = {
            1 : Add,
            2 : Delete,
            3 : Statement,
            4 : Start
        }

    def __str__(self) :
        return 'Income'


class Exit(AbstractMenu) :
    def __str__(self) :
        return 'Exit'

    def use(self) :
        print('Are you sure?[y/n]')
        confirm = input()
        if confirm.lower() == 'y' :
            print('Goodbye.')
            sleep(1)
            quit()

        else :
            print('Good choice.')
            return Start


# from views.menu import Start


class MainMenu :
    def __init__(self) :
        self.options = Start().options
        self.repositories = {}

    def add_options(self, menu_object) :
        self.options = menu_object

    def draw(self) :
        for shortcut, option in self.options.items() :
            print(f'[{shortcut}] - {option()}')

    def isInOption(self, value) :
        return value in self.options

    def findEmpty(self, optionMenu) :
        return len(optionMenu) != 0

    def askUser(self) :
        deep = int(input('Choose option: '))
        while not self.isInOption(deep) :
            print(f'{deep} does not exists...\n    Try again.')
            deep = int(input('Choose option: '))
        return self.options[deep]()

    def setMenu(self) :
        choice = self.askUser()
        if self.findEmpty(choice.options) :
            return self.add_options(choice.options)
        return choice.use()

    # def set_repository(self, name, repository):
    #     return self.repositories[name] = repository
