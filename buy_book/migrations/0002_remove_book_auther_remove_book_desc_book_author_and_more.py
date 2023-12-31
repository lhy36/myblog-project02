# Generated by Django 4.1.7 on 2023-11-06 20:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("buy_book", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="book",
            name="auther",
        ),
        migrations.RemoveField(
            model_name="book",
            name="desc",
        ),
        migrations.AddField(
            model_name="book",
            name="author",
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="book",
            name="delivery_info",
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="book",
            name="stock",
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="book",
            name="amount",
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name="book",
            name="date",
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name="book",
            name="publisher",
            field=models.CharField(max_length=100),
        ),
    ]
