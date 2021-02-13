from django.contrib import admin
from . import models


# Register your models here.

@admin.register(models.Book)
class BookCoustom(admin.ModelAdmin):
    pass


@admin.register(models.Author)
class AuthorCoustom(admin.ModelAdmin):
    pass

