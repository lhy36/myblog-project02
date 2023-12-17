# from django.db import models
# from django.contrib.auth.models import User
# from book.models import *

# class Book(models.Model):
#     name = models.CharField(max_length=100)
#     author = models.CharField(max_length=100)  # 저자 정보 추가
#     publisher = models.CharField(max_length=100)  # 출판사 정보 추가
#     date = models.DateField()  # 출판일 정보 추가
#     image = models.ImageField(upload_to='image')
#     amount = models.DecimalField(max_digits=10, decimal_places=2)  # 가격 정보 추가
#     stock = models.PositiveIntegerField()  # 재고 정보 추가
#     delivery_info = models.CharField(max_length=100)  # 배송 정보 추가


#     def __str__(self):
#         return self.name