from unittest import TestCase

from .Account import Account
from .MyCustomException import MyCustomException


class TestAccount(TestCase):

        def setUp(self) -> None:
            self.acc = Account("Elder Jega", 1379)

        def test_account_can_be_created(self):
            # acc = Account()
            self.assertIsNotNone(self.acc)

        def test_that_account_has_zero_balance_on_creation(self):
            # acc = Account()
            self.assertEqual(0, self.acc.balance)

        def test_that_account_has_a_name(self):
            # acc = Account("Elder Jega")

            self.assertEqual("Elder Jega", self.acc.name)

        def test_deposit_money_balance_increases(self):
            self.acc.deposit(10000)
            self.assertEqual(10000, self.acc.balance)

        def test_withdraw_money_balance_decreases(self):
            self.acc.deposit(10000)
            self.acc.withdraw(3000)
            self.assertEqual(7000, self.acc.balance)

        def test_that_balance_cant_increase_when_negative_amount_deposited(self):
            with self.assertRaises(MyCustomException):
                self.acc.deposit(-10000)
                self.assertEqual(0, self.acc.balance)


        def test_that_money_cant_be_withdrawn_with_negative_amount(self):
            with self.assertRaises(MyCustomException):
                self.acc.withdraw(-4000)








