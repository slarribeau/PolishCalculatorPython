from unittest import TestCase
import decimal
from  Calculator import Calculator


class CalculatorWithThreeValuesTest(TestCase):

    def setUp(self):
        self.calculator = Calculator();
        self.value1 = decimal.Decimal(12);
        self.value2 = decimal.Decimal(22);
        self.value3 = decimal.Decimal(52);

        self.calculator.setAccumulator(self.value1);
        self.calculator.enter();

        self.calculator.setAccumulator(self.value2);
        self.calculator.enter();

        self.calculator.setAccumulator(self.value3);

    def testAccumulatorAfterPushingThreeValues(self):
        self.assertEqual(self.value3, self.calculator.getAccumulator())

    def testAccumulatorAfterSingleDrop(self):
        self.calculator.drop();
        self.assertEqual(self.value2, self.calculator.getAccumulator());

    def testAccumulatorAfterTwoDrops(self):
        self.calculator.drop();
        self.calculator.drop();
        self.assertEqual(self.value1, self.calculator.getAccumulator());
