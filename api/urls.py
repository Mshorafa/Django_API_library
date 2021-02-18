from django.urls import path
from . import views

app_name = 'api'
urlpatterns = [
    path('todocompletedlist/', views.TodoCompletedList.as_view(), name='Todo-Completed-List'),
    path('todocreatelist/', views.TodoCreateList.as_view(), name='Todo-crete-List'),
    path('retrieveupdatedestroy/<int:pk>', views.RetrieveUpdateDestroy.as_view(), name='Todo-rude-List'),
    path('<int:pk>/completed/', views.TodoUpdatedCompleted.as_view(), name='Todo-update-completed-List'),
    path('singup/', views.SingUp, name='singup'),
    path('lgoin/', views.lgoin, name='lgoin'),
]
