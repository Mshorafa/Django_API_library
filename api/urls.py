from django.urls import path
from . import views as todo_view
from expenses import views as expenses_view

app_name = "api"
urlpatterns = [
    # Todo_App
    path(
        "todocompletedlist/",
        todo_view.TodoCompletedList.as_view(),
        name="Todo-Completed-List",
    ),
    path("todocreatelist/", todo_view.TodoCreateList.as_view(), name="Todo-crete-List"),
    path(
        "retrieveupdatedestroy/<int:pk>",
        todo_view.RetrieveUpdateDestroy.as_view(),
        name="Todo-rude-List",
    ),
    path(
        "<int:pk>/completed/",
        todo_view.TodoUpdatedCompleted.as_view(),
        name="Todo-update-completed-List",
    ),
    path("singup/", todo_view.SingUp, name="singup"),
    path("lgoin/", todo_view.lgoin, name="lgoin"),
    # Expanses_App
    path(
        "expenses/",
        expenses_view.ExpensesCreateView.as_view(),
        name="expenses-list-create",
    ),
    path(
        "expensesretrieveanddelete/<int:pk>",
        expenses_view.ExpensesRetrieveAndDelete.as_view(),
        name="Expenses-Retrieve-AndDelete",
    ),
]
