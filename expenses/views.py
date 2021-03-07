from rest_framework.generics import RetrieveDestroyAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_api_key.permissions import HasAPIKey
from . import models, serializers

# Create your views here.


class ExpensesCreateView(ListCreateAPIView):
    serializer_class = serializers.ExpenseSserializer
    queryset = models.Expense.objects.all()
    filterset_fields = ["categroy", "merchent"]
    permission_classes = [HasAPIKey]


class ExpensesRetrieveAndDelete(RetrieveDestroyAPIView):
    serializer_class = serializers.ExpenseSserializer
    queryset = models.Expense.objects.all()
    permission_classes = [HasAPIKey]
