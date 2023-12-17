from django.contrib import admin
from django.urls import path, include
from book.views import *
from book.models import *
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import *


urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('book.urls')),
    path('admin_panel', include("admin_panel.urls")),
    path('buy', include("buy_book.urls")),
    path('add', include('add_book.urls')),
    path('used', include('used_book.urls')),
    path('my_info', include('my_info.urls')),
    # path('subdepartment/<str:subdepartment>/', books_sub, name='books_sub'),
    # path('department/<str:department_name>/', department_books, name='department_books'),
    path('pay', include("book_pay.urls")),
]+static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

