from django.test import TestCase
from .models import Expense
from django.urls import reverse


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


class TestViews(TestCase):
    def test_expenses_create(self):
        payload = {
            "amount": 50,
            "merchent": "AT&T",
            "decreption": "cell phone subscription",
            "categroy": "utilities",
        }

        res_post = self.client.post(
            reverse("api:expenses-list-create"), payload, format="json"
        )
        self.assertEqual(201, res_post.status_code)

        json_res = res_post.json()

        self.assertEqual(str(payload["amount"]), json_res["amount"])
        self.assertEqual(payload["merchent"], json_res["merchent"])
        self.assertEqual(payload["decreption"], json_res["decreption"])
        self.assertEqual(payload["categroy"], json_res["categroy"])
        self.assertIsInstance(json_res["id"], int)

    def test_expenses_list(self):
        res_get = self.client.get(reverse("api:expenses-list-create"), format="json")
        self.assertEqual(200, res_get.status_code)
        json_res = res_get.json()
        self.assertIsInstance(json_res, list)
        expenses = Expense.objects.all()
        self.assertEqual(len(expenses), len(json_res))
