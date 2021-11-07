from abc import ABC, abstractmethod
from time import sleep
from csv import reader, writer


#----------------------------------------------repositories.py---------------------------------------------------------
class Repositories:
    def __init__(self):
        newData = []

    def is_User(self,first_name, last_name):
        id = 0
        with open('example.csv','r',encoding='utf-8') as checkFile:
            checkUserList = reader(checkFile,declimiter=',')
            next(checkUserList)
            for user in checkUserList:
                if first_name.lower() == user[1] and last_name.lower() == user[2]:
                    id = user[0]

        return id


#-----------------------------------------------actions.py-------------------------------------------------------------
class Add:
    def __str__(self):
        return 'Add'



class Delete:
    def __str__(self):
        return 'Delete'


class Statement:
    def __str__(self):
        return 'Show'

#--------------------------------------------Menu.py-------------------------------------------------------------------
class AbstractMenu(ABC):
    def __init__(self):
        self.options ={}

    @abstractmethod
    def __str__(self):
        pass


class People(AbstractMenu):
    def __init__(self):
        super().__init__()
        self.options = {
            1: Add,
            2: Delete,
            3: Statement,
            4: Start
        }

    def __str__(self):
        return'People'


class Income(AbstractMenu):
    def __init__(self):
        super().__init__()
        self.options = {
            1: Add,
            2: Delete,
            3: Statement,
            4: Start
        }

    def __str__(self):
        return 'Income'


#---------------------------------------------------Exit.py------------------------------------------------------------
class Exit(AbstractMenu):
    def __str__(self):
        return 'Exit'

    def use(self):
        super().use()
        print('Are you shure?[y/n]')
        confirm = input()
        if confirm.lower() == 'y':
            print('Goodbye.')
            sleep(1)
            quit()

        else:
            print('Good choice.')


#----------------------------------------------Mainmenu.py-------------------------------------------------------------
class Start(AbstractMenu):
    def __init__(self):
        super().__init__()
        self.options = {
            1: People,
            2: Income,
            3: Exit
        }

    def __str__(self):
        return 'Main Menu'


class MainMenu:
    def __init__(self):
        self.options = Start().options

    def add_options(self, menu_object):
        self.options = menu_object

    def draw(self):
        for shortcut, option in self.options.items():
            print(f'[{shortcut}] - {option()}')

    def setMenu(self):
        deep = int(input('Choose option: '))
        choice = self.options[deep]()
        return self.add_options(choice.options)


#-----------------------------------------------------Application.py---------------------------------------------------
class Application:
    def startMenu(self):
        menu = MainMenu()
        while True:
            menu.draw()
            menu.setMenu()




#-------------------------------------------------------Main.py--------------------------------------------------------

if __name__ == '__main__':
    app = Application()
    app.startMenu()
