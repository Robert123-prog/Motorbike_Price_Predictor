from backend.controller.Controller import Controller

class Tests:
    def __init__(self):
        self.controller = Controller()
        self.motorcycles = self.controller.motorcycles

    def test_motorcycle_selection(self):
        self.controller.select_motorcycle()
        index = int(input())

        assert(self.motorcycles.get(index) == self.controller.motorcycles.get(index))

    def test_year_selection(self):
        self.controller.select_motorcycle_year()
        year = int(input())



