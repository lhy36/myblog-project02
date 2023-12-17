from django.urls import path
from . import views



urlpatterns = [
    path('', views.my_info, name='my_info'),
    path('/cart', views.cart, name='cart'),
    path('/heart', views.heart, name='heart'),
    path('/my_info_app_url/', views.my_info_view, name='my_info_app'),
    # path('add_cart/<int:product_id>/', views.add_cart, name='add_cart'),

    # path('my_info/', include('my_info.urls')),
]