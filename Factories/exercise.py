"""
You are given a class called Person . The person has two attributes: id , and name .

Please implement a  PersonFactory that has a non-static  create_person()  method that takes a person's name and return a person initialized with this name and an id.

The id of the person should be set as a 0-based index of the object created. So, the first person the factory makes should have Id=0, second Id=1 and so on.
"""
from unittest import TestCase


class Person:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class PersonFactory:
    id = 0

    def create_person(self, name):
        p = Person(PersonFactory.id, name)
        PersonFactory.id += 1
        return p

class Evaluate(TestCase):
    def test_exercise(self):
        pf = PersonFactory()

        p1 = pf.create_person('Chris')
        self.assertEqual(p1.name, 'Chris')
        self.assertEqual(p1.id, 0)

        p2 = pf.create_person('Sarah')
        self.assertEqual(p2.id, 1)
