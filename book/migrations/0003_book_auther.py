# Generated by Django 4.1.7 on 2023-08-13 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("book", "0002_book_date_book_publisher"),
    ]

    operations = [
        migrations.AddField(
            model_name="book",
            name="auther",
            field=models.CharField(default="timezone.now", max_length=500),
            preserve_default=False,
        ),
    ]