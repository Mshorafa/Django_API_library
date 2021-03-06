from rest_framework import serializers
from . import models


class ExpenseSserializer(serializers.ModelSerializer):
    amount = serializers.FloatField(required=True)
    merchent = serializers.CharField(required=True)
    decreption = serializers.CharField(required=True)
    categroy = serializers.CharField(required=True)
    date_created = serializers.DateTimeField(required=False)
    updated_created = serializers.DateTimeField(required=False)

    class Meta:
        model = models.Expense
        fields = "__all__"
        read_only_fields = ["id", "date_created", "updated_created"]
