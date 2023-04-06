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
