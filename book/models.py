from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=100)
    amount = models.IntegerField()
    desc = models.TextField(max_length=1000)
    image = models.ImageField(upload_to='image')
    publisher = models.CharField(max_length=500)
    author = models.CharField(max_length=500)  # 오타 수정
    date = models.DateTimeField(auto_now=True)
    stock = models.PositiveIntegerField(default=0)  # 수량 필드 추가


    def __str__(self):
        return self.name
    
class Department(models.Model):
    name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name
    
class SubDepartment(models.Model):
    name = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    booklist = models.ManyToManyField(Book, related_name='booklist', blank=True)
    
    def __str__(self):
        return self.name
