class Animal:
    def fly():
        pass
    def run():
        pass
    def bark():
        pass


class Dog(Animal):
    def fly():
        pass

    def run():
        print('Dog is running')

    def bark():
        print("Dog is barking")


class Bird(Animal):
    def fly():
        print('Bird is flying')

    def run():
        print('Bird is running')

    def bark():
        pass
