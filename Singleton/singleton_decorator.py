"""
The decorator takes in the class as parameter and new instance is created only if an instance already exists.
When a new object is created, instance of the old object is assigned to the new object
It satisfies the singleton principle
"""
def singleton(class_):
    instances = {}

    def get_instance(*args, **kwargs):
        print(instances)
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]

    return get_instance


@singleton
class Database:
    def __init__(self):
        print('Loading database')


if __name__ == '__main__':
    d1 = Database()
    d2 = Database()
    print(d1 == d2)