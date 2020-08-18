from random import choice


class Person:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "Hello {name}!".format(name=self.name)


def people_choice():
    people = [
        Person("Sam"),
        Person("Jack"),
        Person("Bob")
    ]
    person = choice(people)
    print(person)

