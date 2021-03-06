from django.shortcuts import render
from django.forms.models import model_to_dict

from rest_framework.views import APIView
from rest_framework.response import Response

from . import models, serializers


# Create your views here.


class ExpensesCreateView(APIView):
    def get(self, request):
        expenses = models.Expense.objects.all()
        serializer = serializers.ExpenseSserializer(expenses, many=True)
        return Response(serializer.data, status=200)

    def post(self, request):
        serializer = serializers.ExpenseSserializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=201)
