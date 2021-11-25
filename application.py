from views.menu import MainMenu
from controllers.repositories import UserRepository


class Application:
    def startMenu(self):
        menu = MainMenu()
        while True:
            menu.draw()
            menu.setMenu()