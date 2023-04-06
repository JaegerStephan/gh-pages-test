class User:
    """
    This is a class containing some attributes of the user 
    with corresponding setters and getters
    """
    def __init__(self, name, id, birthday):
        self._name = name
        self._id = id
        self._birthday = birthday

    # Setters
    def set_name(self, name):
        self._name = name

    def set_id(self, id):
        self._id = id

    def set_birthday(self, birthday):
        self._birthday = birthday

    # Getters
    def get_name(self):
        return self._name

    def get_id(self):
        return self._id

    def get_birthday(self):
        return self._birthday


def main():
    # Create an object of User class
    user1 = User("Alice", 12345, "1995-06-15")

    # Accessing attributes using getters
    print("Name: ", user1.get_name())
    print("ID: ", user1.get_id())
    print("Birthday: ", user1.get_birthday())

    # Modifying attributes using setters
    user1.set_name("Alicia")
    user1.set_id(54321)
    user1.set_birthday("1995-06-16")

    # Accessing attributes again after modification
    print("Name: ", user1.get_name())
    print("ID: ", user1.get_id())
    print("Birthday: ", user1.get_birthday())


if __name__ == "__main__":
    main()