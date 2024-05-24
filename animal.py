class Animal:
    def __init__(self):
        print("Animal created..")


class Fish(Animal):
    def __init__(self):
        super().__init__()
        print("Fish created")


a = Fish()
