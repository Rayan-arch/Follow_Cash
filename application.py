from views.menu import MainMenu


class Application:
    def startMenu(self):
        menu = MainMenu()
        while True:
            menu.draw()
            menu.setMenu()

    def EntryRepository(self):
        return