# Generated by Django 4.2.7 on 2023-12-17 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('used_book', '0015_alter_usedbook_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usedbook',
            name='category',
            field=models.CharField(choices=[('자바스크립트서버플랫폼', '자바스크립트서버플랫폼'), ('4차산업혁명 머신러닝실습', '4차산업혁명 머신러닝실습'), ('파이썬 웹 프로그래밍', '파이썬 웹 프로그래밍'), ('드림업 취업코칭', '드림업 취업코칭')], max_length=50),
        ),
    ]
