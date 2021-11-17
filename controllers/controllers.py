from views.menu import AbstractMenu
from controllers.repositories import Repositories

class Add(AbstractMenu):
    def __str__(self):
        return 'Add'

    def use(self):
        first_name = input('Write your first name: ')
        last_name = input('Write your last name: ')
        user = Repositories()
        if user.isUser(first_name, last_name):
            user.addUser(first_name, last_name)

        return user.insertWorkday()


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
