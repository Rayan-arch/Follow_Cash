from csv import reader, writer, QUOTE_MINIMAL


class UserRepository:
    def __init__(self):
        self.newUserList = []
        with open('./data/example_users.csv', 'r', encoding='utf-8') as checkFile :
            userList = reader(checkFile, delimiter=',')

            for user in userList:
                self.newUserList.append(user)


    def find(self,first_name, last_name):
        id = 0
        for user in self.newUserList:
            if first_name == user[1] and last_name == user[2]:
                id = user[0]

        return int(id)

    def addUser(self, first_name, last_name):
        id = len(self.newUserList)

        with open('./data/example_users.csv', 'w', encoding='utf-8', newline='') as saveFile:
            new = writer(saveFile, delimiter=',')
            self.newUserList.append([str(id), first_name, last_name])

            for user in self.newUserList:
                new.writerow(user)

        print('User added successful')

    def deleteUser(self, first_name, last_name):
        id = self.find(first_name, last_name)
        if id != 0:
            with open('./data/example_users.csv', 'w', encoding='utf-8', newline='') as deletefile:
                erise = writer(deletefile, delimiter=',')
                self.newUserList.pop(id)
                for user in self.newUserList :
                    erise.writerow(user)

            print('User deleted successful.')

        else:
            print(f"User {self.first_name.capitalize()} {self.last_name.capitalize()} can't be found.")

    def showUsers(self):
        for user in self.newUserList:
            print(f'{user[0]}. {user[1].capitalize()} {user[2].capitalize()}')

    def insertWorkday(self) :
        print('ok')
