# Generated by Django 3.0.5 on 2021-10-30 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_auto_20211029_1652'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='book_age_rating',
            field=models.PositiveIntegerField(default=3),
        ),
        migrations.AddField(
            model_name='book',
            name='book_rating',
            field=models.PositiveIntegerField(default=1),
        ),
    ]