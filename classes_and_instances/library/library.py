class Library:

    def __init__(self):
        self.user_records = []
        self.books_available = {}
        self.rented_books = {}

    def remove_user(self, user):
        if user in self.user_records:
            self.user_records.remove(user)
            if user in self.rented_books:
                del self.rented_books[user]
            return
        return "We could not find such user to remove!"

    def add_user(self, user):
        if user not in self.user_records:
            self.user_records.append(user)
            return
        return f"User with id = {user.user_id} already registered in the library!"

    def change_username(self, user_id: int, new_username: str):
        for u in self.user_records:
            if u.user_id == user_id and u.username != new_username:
                if user_id in self.rented_books:
                    self.rented_books[new_username] = self.rented_books[u.username]
                    del self.rented_books[u.username]
                u.username = new_username
                return f"Username successfully changed to: {new_username} for userid: {user_id}"
            elif u.user_id == user_id and u.username == new_username:
                return "Please check again the provided username - it should be different than the username used so far!"
        return f"There is no user with id = {user_id}!"
