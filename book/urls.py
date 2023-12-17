from django.urls import path
from . import views
# from .views import add_to_cart


urlpatterns=[
    path('', views.home, name='home'),
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('logout',views.logout, name='logout'),
    # path('add_to_cart/<int:book_id>/', views.add_to_cart, name='add_to_cart'),
    # path('cart/', views.cart, name='cart'),
]