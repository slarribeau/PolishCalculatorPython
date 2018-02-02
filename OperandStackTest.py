from unittest import TestCase
import decimal
from OperandStack import OperandStack

class TestOperandStackTest(TestCase):

    def setUp(self):
        self.stack = OperandStack()

    def testNewOperandStackPeekReturnsZero(self):
        self.assertEqual(decimal.Decimal(0), self.stack.peek())

    def testPushingValueOntoStack(self):
        value = decimal.Decimal(12)
        self.stack.push(value)
        self.assertEqual(value, self.stack.peek())

    def testReplacingTopOfSack(self):
        self.stack.push(decimal.Decimal(22))
        value = decimal.Decimal(66)
        self.stack.replaceTop(value)
        self.assertEqual(66, self.stack.peek())

    def testReplacingWithEmptyStack(self):
        value = decimal.Decimal(66)
        self.stack.replaceTop(value)
        self.assertEqual(value,self.stack.peek())

    def testPoppingValuesFromStack(self):
        value = decimal.Decimal(45)
        self.stack.push(value);
        self.stack.push(decimal.Decimal(55));
        self.stack.pop();
        self.assertEqual(value, self.stack.peek());


    def testPoppingEmptyStack(self):
        self.stack.pop()
        self.assertEqual(decimal.Decimal(0), self.stack.peek())



