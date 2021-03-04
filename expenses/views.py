from django.shortcuts import render
from django.forms.models import model_to_dict

from rest_framework.views import APIView
from rest_framework.response import Response

from . import models


# Create your views here.


class ExpensesCreateView(APIView):
    def get(self, request):
        expenses = models.Expense.objects.all()
        all_expense = [model_to_dict(expenses) for expense in expenses]
        return Response(all_expense, status=200)

    def post(self, request):
        amount = request.data.get("amount")
        merchent = request.data.get("merchent")
        decreption = request.data.get("decreption")
        categroy = request.data.get("categroy")
        print(amount, merchent, decreption, categroy)

        expenses_item = models.Expense.objects.create(
            amount=amount, merchent=merchent, decreption=decreption, categroy=categroy
        )

        return Response(model_to_dict(expenses_item), status=201)
