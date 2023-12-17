from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('book', views.book, name='book'),
    path('delete/<int:id>', views.delete, name='name'),
    path('create', views.create, name='create'),
] 