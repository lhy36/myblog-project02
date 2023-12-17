# Generated by Django 4.1.7 on 2023-08-13 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("book", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="book",
            name="date",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name="book",
            name="publisher",
            field=models.CharField(default="timezone.now", max_length=500),
            preserve_default=False,
        ),
    ]