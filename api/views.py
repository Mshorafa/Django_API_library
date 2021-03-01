from django.contrib.auth.models import User
from django.db import IntegrityError
from django.shortcuts import redirect, render
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import generics, permissions
from rest_framework.authtoken.models import Token
from django.http import JsonResponse
from django.contrib.auth import login, logout, authenticate
from todowoo import models
from . import serializers


@csrf_exempt
def SingUp(request):
    if request.method == "POST":
        try:
            data = JSONParser().parse(request)
            user = User.objects.create_user(
                username=data["username"], password=data["password1"]
            )
            user.save()
            token = Token.objects.create(user=user)
            return JsonResponse({"token": str(token)}, status=201)
        except IntegrityError:
            return JsonResponse(
                {
                    "error": "That username has already been taken. Please choose a new username"
                },
                status=400,
            )


@csrf_exempt
def lgoin(request):
    if request.method == "POST":
        data = JSONParser().parse(request)
        user = authenticate(
            request, username=data["username"], password=data["password"]
        )
        if user is None:
            return JsonResponse(
                {
                    "error": "could not login Please check the user name and the password"
                },
                status=400,
            )
        else:
            try:
                token = Token.objects.get(user=user)
            except:
                token = Token.objects.create(user=user)
            return JsonResponse({"token": str(token)}, status=201)


class TodoCompletedList(generics.ListAPIView):
    serializer_class = serializers.TodoListsSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        todo = models.Todo.objects.filter(
            user=user, datecompleted__isnull=False
        ).order_by("-datecompleted")
        return todo


class TodoCreateList(generics.ListCreateAPIView):
    serializer_class = serializers.TodoListsSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        todo = models.Todo.objects.filter(user=user, datecompleted__isnull=True)
        return todo

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class RetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.TodoListsSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        todo = models.Todo.objects.filter(user=user)
        return todo


class TodoUpdatedCompleted(generics.UpdateAPIView):
    serializer_class = serializers.TodoCompletedSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        todo = models.Todo.objects.filter(user=user)
        return todo

    def perform_update(self, serializer):
        serializer.instance.datecompleted = timezone.now()
        serializer.save()
