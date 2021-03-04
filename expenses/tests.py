from django.test import TestCase
from .models import Expense


# Create your tests here.
class TestModel(TestCase):
    def test_Expense(self):
        expenac = Expense.objects.create(
            amount=349.99,
            merchent="Amazon",
            decreption="anc head phones",
            categroy="music",
        )
        incerated_expense = Expense.objects.get(pk=expenac.id)

        self.assertEqual(349.99, incerated_expense.amount)
        self.assertEqual("Amazon", incerated_expense.merchent)
        self.assertEqual("anc head phones", incerated_expense.decreption)
        self.assertEqual("music", incerated_expense.categroy)
