from csv import reader, writer


class Repositories:
    def __init__(self):
        newData = []

    def isUser(self, first_name, last_name):
        id = 0
        with open('../data/example.csv', 'r', encoding='utf-8') as checkFile:
            checkUserList = reader(checkFile)
            next(checkUserList)
            for user in checkUserList:
                if first_name.lower() == user[1] and last_name.lower() == user[2]:
                    id = user[0]

        return id

    def addUser(self, first_name: str, last_name: str):
        if self.isUser(first_name, last_name):
            pass

    def insertWorkday(self):
        print('ok')
