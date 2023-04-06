from model.user import User

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