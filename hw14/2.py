import unittest

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

class User:
    def __init__(self, name, user_id, level):
        self.name = name
        self.user_id = user_id
        self.level = level

    def __str__(self):
        return f"User: {self.name}, ID: {self.user_id}, Level: {self.level}"

class TestUserManager(unittest.TestCase):
    def setUp(self):
        self.user_manager = UserManager()
        self.user_manager.add_user("John Doe", 1, 3)
        self.user_manager.add_user("Alice Johnson", 2, 5)
        self.user_manager.add_user("Bob Smith", 3, 2)

    def test_add_user(self):
        self.user_manager.add_user("Eva Brown", 4, 4)
        self.assertEqual(len(self.user_manager.users), 4)

    def test_change_level_valid_user(self):
        self.assertTrue(self.user_manager.change_level(2, 4))
        self.assertEqual(self.user_manager.users[1].level, 4)

    def test_change_level_invalid_user(self):
        self.assertFalse(self.user_manager.change_level(5, 4))

    def test_display_users(self):
        expected_output = "User: John Doe, ID: 1, Level: 3\n" \
                          "User: Alice Johnson, ID: 2, Level: 5\n" \
                          "User: Bob Smith, ID: 3, Level: 2\n"
        with self.assertLogs() as log:
            self.user_manager.display_users()
            self.assertEqual(log.output, [f"INFO:root:{expected_output}"])

if __name__ == '__main__':
    unittest.main()
