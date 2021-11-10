from abc import ABC, abstractmethod
from time import sleep
from csv import reader, writer


#----------------------------------------------repositories.py---------------------------------------------------------
class Repositories:
    def __init__(self):
        newData = []

    def isUser(self,first_name, last_name):
        id = 0
        with open('example.csv','r',encoding='utf-8') as checkFile:
            checkUserList = reader(checkFile,declimiter=',')
            next(checkUserList)
            for user in checkUserList:
                if first_name.lower() == user[1] and last_name.lower() == user[2]:
                    id = user[0]

        return id

    def addUser(self, first_name: str, last_name: str):
        if isUser():
            pass



#-----------------------------------------------actions.py-------------------------------------------------------------
class AbstractMenu(ABC):
    def __init__(self):
        self.options ={}

    @abstractmethod
    def __str__(self):
        pass

class Add(AbstractMenu):
    def __str__(self):
        return 'Add'

    def use(self):
        first_name = input('Write your first name: ')
        last_name = input('Write your last name: ')
        user = Repositories()
        if user.isUser(first_name, last_name):
            user.addUser()


class Delete(AbstractMenu):
    def __str__(self):
        return 'Delete'

    def use(self):
        pass


class Statement(AbstractMenu):
    def __str__(self):
        return 'Show'

    def use(self):
        pass

#--------------------------------------------Menu.py-------------------------------------------------------------------
class People(AbstractMenu):
    def __init__(self):
        # super().__init__()
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
        # super().__init__()
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
    # def __init__(self):
    #     super().__init__()
    #     self.options = {
    #         0: self.use()
    #     }

    def __str__(self):
        return 'Exit'

    def use(self):
        print('Are you shure?[y/n]')
        confirm = input()
        if confirm.lower() == 'y':
            print('Goodbye.')
            sleep(1)
            quit()

        else:
            print('Good choice.')
            return Start


#----------------------------------------------Mainmenu.py-------------------------------------------------------------
class Start(AbstractMenu):
    def __init__(self):
        # super().__init__()
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

    def isInOption(self,value):
        return value in self.options

    def findEmpty(self,optionMenu):
        return len(optionMenu) != 0

    def askUser(self):
        deep = int(input('Choose option: '))
        while not self.isInOption(deep):
            print(f'{deep} does not exists...\n    Try again.')
            deep = int(input('Choose option: '))
        return self.options[deep]()

    def setMenu(self):
        choice = self.askUser()
        if self.findEmpty(choice.options):
            return self.add_options(choice.options)
        return choice.use()



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
