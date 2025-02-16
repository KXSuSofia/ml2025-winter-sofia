class NumberBox:
    def __init__(self):
        self.numbers = []

    def add_number(self, number):
        self.numbers.append(number)

    def find_number(self, target):
        if target in self.numbers:
            return self.numbers.index(target) + 1  
        else:
            return -1
