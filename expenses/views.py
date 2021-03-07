from rest_framework.generics import RetrieveDestroyAPIView, ListCreateAPIView
from . import models, serializers

# Create your views here.


class ExpensesCreateView(ListCreateAPIView):
    serializer_class = serializers.ExpenseSserializer
    queryset = models.Expense.objects.all()


class ExpensesRetrieveAndDelete(RetrieveDestroyAPIView):
    serializer_class = serializers.ExpenseSserializer
    queryset = models.Expense.objects.all()
