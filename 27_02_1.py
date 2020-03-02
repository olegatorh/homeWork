import random


class Ghost(object):
    def __init__(self):
        colors = ['white', 'yellow', 'purple', 'red']
        self.__dict__["color"] = (random.choice(colors))


user = Ghost()
print(user.__dict__)
