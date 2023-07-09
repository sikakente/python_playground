import collections


class Employee:
    def __init__(self, name, birth_date):
        self._name = name
        self._birthdate = birth_date

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value


collections.deque()

if __name__ == '__main__':
    for count, value in enumerate(range(19)):
        print(count, value)
