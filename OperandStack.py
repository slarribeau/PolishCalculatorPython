import decimal
class OperandStack:

    def __init__(self):
        self.values =  [];

    def push(self, value):
        self.values.append(value)

    def peek(self):
        if (len(self.values) == 0):
            return decimal.Decimal(0)
        return (self.values[-1])

    def pop(self):
        if (len(self.values) > 0):
            self.values.pop()

    def replaceTop(self, value):
        self.pop()
        self.push(value)
