class Greet:
    def __init__(self, name, new_user: bool = False):
        self.newbie = new_user
        self.name = name

    def say_hi(self):
        if self.newbie == True:
           greet = 'Welcome'
        else:
           greet = 'Hi'
        return greet + self.name

