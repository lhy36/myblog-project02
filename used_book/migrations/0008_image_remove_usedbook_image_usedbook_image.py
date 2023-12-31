# Generated by Django 4.1.7 on 2023-11-30 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("used_book", "0007_alter_usedbook_image_delete_comment"),
    ]

    operations = [
        migrations.CreateModel(
            name="Image",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("file", models.ImageField(upload_to="books/")),
            ],
        ),
        migrations.RemoveField(
            model_name="usedbook",
            name="image",
        ),
        migrations.AddField(
            model_name="usedbook",
            name="image",
            field=models.ManyToManyField(related_name="books", to="used_book.image"),
        ),
    ]
