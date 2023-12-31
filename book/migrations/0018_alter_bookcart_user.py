# Generated by Django 4.1.7 on 2023-10-24 05:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('book', '0017_bookcart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookcart',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='book_carts', to=settings.AUTH_USER_MODEL),
        ),
    ]
