from rest_framework.generics import RetrieveDestroyAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from . import models, serializers

# Create your views here.


class ExpensesCreateView(ListCreateAPIView):
    serializer_class = serializers.ExpenseSserializer
    queryset = models.Expense.objects.all()
    filterset_fields = ["categroy", "merchent"]
    permission_classes = [IsAuthenticated]


class ExpensesRetrieveAndDelete(RetrieveDestroyAPIView):
    serializer_class = serializers.ExpenseSserializer
    queryset = models.Expense.objects.all()
