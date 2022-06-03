from django.urls import path
from . import views
app_name = 'polls'
urlpatterns = [
    path("", views.index, name='index'),
    path("list",views.viewsQuestion, name="views_list"),
    path("detatel/<int:question_id>",views.detalViews, name="detatel"),
    path("<int:question_id>", views.vote, name="vote"),
]