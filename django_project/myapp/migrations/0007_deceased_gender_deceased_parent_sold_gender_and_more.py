# Generated by Django 5.0.3 on 2024-03-20 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_deceased_sold'),
    ]

    operations = [
        migrations.AddField(
            model_name='deceased',
            name='gender',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='deceased',
            name='parent',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='sold',
            name='gender',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='sold',
            name='parent',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
