class User:
    def __init__(self, name, user_id, level=None):
        self.name = name
        self.user_id = user_id
        self.level = level

    def __eq__(self, other):
        return self.user_id == other.user_id and self.name == other.name

    def __repr__(self):
        return f'{self.name}'
