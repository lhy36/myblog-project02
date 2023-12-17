from django.urls import path
from . import views

urlpatterns = [
    path('', views.add, name='add'),
    path('', views.bookadd_bookadd_changelist, name='bookadd_bookadd_changelist'),
]