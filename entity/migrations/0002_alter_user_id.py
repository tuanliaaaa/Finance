# Generated by Django 4.2.6 on 2024-08-30 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entity', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.BigIntegerField(auto_created=True, primary_key=True, serialize=False),
        ),
    ]
