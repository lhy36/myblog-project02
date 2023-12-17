from django.db import models
from django.contrib.auth.models import User
from django.db import models
class DetailImage(models.Model):
    image = models.ImageField(upload_to='books/images/')
    used_book = models.ForeignKey('UsedBook', on_delete=models.CASCADE, related_name='images') 

    def __str__(self):
        return f"Image {self.pk}"
class UsedBook(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    image = models.ImageField(upload_to='books/', null=True)
    # detail_image = models.ForeignKey(DetailImage, on_delete=models.CASCADE, related_name='used_books', null=True)
    detail_images = models.ManyToManyField(DetailImage)
    category = models.CharField(max_length=50, choices=[
        ('자바스크립트서버플랫폼', '자바스크립트서버플랫폼'),
        ('4차산업혁명 머신러닝실습', '4차산업혁명 머신러닝실습'),
        ('파이썬 웹 프로그래밍', '파이썬 웹 프로그래밍'),
        ('드림업 취업코칭', '드림업 취업코칭'),
    
        
    ])
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.title



class Comment(models.Model):
    userid = models.CharField(max_length=255)
    content = models.TextField()
    date = models.DateField()

    def __str__(self):
        return f'{self.userid} - {self.date}'