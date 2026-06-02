class User:
    count = 0
    
    def __init__(self, name, login, password, grade):
        self.__name = name
        self.__login = login
        self.__password = password
        self.__grade = grade
        User.count += 1
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        self.__name = value
    
    @property
    def login(self):
        return self.__login
    
    @login.setter
    def login(self, value):
        print("Невозможно изменить логин!")
    
    @property
    def password(self):
        return "********"
    
    @password.setter
    def password(self, value):
        self.__password = value
    
    @property
    def grade(self):
        return "Неизвестное свойство grade"
    
    @grade.setter
    def grade(self, value):
        print("Неизвестное свойство grade")
    
    def show_info(self):
        print(f"Name: {self.__name}, Login: {self.__login}")
    
    def __eq__(self, other):
        if isinstance(other, User):
            return self.__grade == other.__grade
        return NotImplemented
    
    def __lt__(self, other):
        if isinstance(other, User):
            return self.__grade < other.__grade
        return NotImplemented
    
    def __gt__(self, other):
        if isinstance(other, User):
            return self.__grade > other.__grade
        return NotImplemented
    
    def eq(self, other):
        return self.__eq__(other)
    
    def lt(self, other):
        return self.__lt__(other)
    
    def gt(self, other):
        return self.__gt__(other)


class SuperUser(User):
    count = 0
    
    def __init__(self, name, login, password, role, grade):
        super().__init__(name, login, password, grade)
        self.__role = role
        SuperUser.count += 1
        User.count -= 1
    
    @property
    def role(self):
        return self.__role
    
    @role.setter
    def role(self, value):
        self.__role = value
    
    def show_info(self):
        print(f"Name: {self.name}, Login: {self.login}, Role: {self.__role}")


# Тестирование
if __name__ == "__main__":
    user1 = User('Paul McCartney', 'paul', '1234', 3)
    user2 = User('George Harrison', 'george', '5678', 2)
    user3 = User('Richard Starkey', 'ringo', '8523', 3)
    admin = SuperUser('John Lennon', 'john', '0000', 'admin', 5)

    user1.show_info()
    admin.show_info()

    users = User.count
    admins = SuperUser.count

    print(f'Всего обычных пользователей: {users}')
    print(f'Всего супер-пользователей: {admins}')

    print(user1 < user2)
    print(admin > user3)
    print(user1 == user3)

    user3.name = 'Ringo Star'
    user1.password = 'Pa$$w0rd'

    print(user3.name)
    print(user2.password)
    print(user2.login)

    user2.login = 'geo'

    print(user1.grade)
    admin.grade = 10
