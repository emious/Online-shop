# Generated by Django 5.1.3 on 2024-12-26 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_alter_attribute_applicable_categories'),
    ]

    operations = [
        migrations.AddField(
            model_name='productreview',
            name='title',
            field=models.CharField(default='', max_length=255),
        ),
    ]