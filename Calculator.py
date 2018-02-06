from OperandStack import OperandStack

class Calculator:
    def __init__(self):
        self.values = OperandStack()

    def setAccumulator(self, value):
        self.values.replaceTop(value);

    def enter(self):
        self.values.push(self.getAccumulator())

    def drop(self):
        self.values.pop()


    def getAccumulator(self):
        return self.values.peek()
