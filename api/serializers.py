from rest_framework import serializers
from todowoo import models


class TodoListsSerializer(serializers.ModelSerializer):
    created = serializers.ReadOnlyField()
    datecompleted = serializers.ReadOnlyField()

    class Meta:
        model = models.Todo
        fields = [
            'id',
            'title',
            'memo',
            'created',
            'datecompleted',
            'important',
        ]


class TodoCompletedSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Todo
        fields = ['id']
        read_oly_fields = [
            'title',
            'memo',
            'created',
            'datecompleted',
            'important',
        ]
