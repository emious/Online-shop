# Generated by Django 5.1.3 on 2024-12-06 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='information',
            field=models.TextField(blank=True),
        ),
    ]