from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)  # 저자 정보 추가
    publisher = models.CharField(max_length=100)  # 출판사 정보 추가
    date = models.DateField()  # 출판일 정보 추가
    image = models.ImageField(upload_to='image')
    amount = models.IntegerField()  # 가격 정보 추가
    stock = models.PositiveIntegerField()  # 재고 정보 추가
    delivery_info = models.CharField(max_length=100)  # 배송 정보 추가


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
    
class buy_detail():
    
    def __str__(self) :
        return self.name

class Heart(models.Model):
    name = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='hearted_books')
    author = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='hearted_users')

    def __str__(self):
        return f"Hearted by {self.name.name} for {self.author.author}"
