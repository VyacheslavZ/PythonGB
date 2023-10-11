class User:
    def __init__(self, name, user_id, level):
        self.name = name
        self.user_id = user_id
        self.level = level

    def __str__(self):
        return f"User: {self.name}, ID: {self.user_id}, Level: {self.level}"

class UserManager:
    def __init__(self):
        self.users = []

    def add_user(self, name, user_id, level):
        new_user = User(name, user_id, level)
        self.users.append(new_user)

    def change_level(self, user_id, new_level):
        for user in self.users:
            if user.user_id == user_id:
                user.level = new_level
                return True
        return False

    def display_users(self):
        for user in self.users:
            print(user)

# Пример использования
user_manager = UserManager()

# Добавление пользователей
user_manager.add_user("John Doe", 1, 3)
user_manager.add_user("Alice Johnson", 2, 5)
user_manager.add_user("Bob Smith", 3, 2)

# Вывод информации о пользователях
print("Initial User List:")
user_manager.display_users()

# Изменение уровня пользователя
user_manager.change_level(2, 4)

# Вывод обновленной информации о пользователях
print("\nUpdated User List:")
user_manager.display_users()
