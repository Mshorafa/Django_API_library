from django.contrib import admin
from .models import Posts, Votes


# Register your models here.


@admin.register(Posts)
class PostsCoutom(admin.ModelAdmin):
    pass


@admin.register(Votes)
class VotesCoutom(admin.ModelAdmin):
    pass
