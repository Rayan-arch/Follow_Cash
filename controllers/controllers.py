from views.AbstracMenus import AbstractMenu, AbstractInteraction
from controllers.repositories import UserRepository

class Add(AbstractInteraction):
    def __str__(self):
        return 'Add'

    def use(self):
        first_name = input('Write your first name: ').lower()
        last_name = input('Write your last name: ').lower()
        user = UserRepository()

        if user.find(first_name, last_name) == 0:
            user.addUser(first_name, last_name)
        else:
            print('User already exists.')

        # return user.insertWorkday()


class Delete(AbstractInteraction):
    def __str__(self):
        return 'Delete'

    def use(self):
        first_name = input('Write your first name: ').lower()
        last_name = input('Write your last name: ').lower()
        user = UserRepository()
        user.deleteUser(first_name, last_name)


class Statement(AbstractInteraction):
    def __str__(self):
        return 'Show'

    def use(self):
        allUsers = UserRepository()
        allUsers.showUsers()
