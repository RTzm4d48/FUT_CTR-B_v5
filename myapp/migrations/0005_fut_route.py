# Generated by Django 4.2 on 2023-06-05 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_fut_n_ticket_fut_view'),
    ]

    operations = [
        migrations.AddField(
            model_name='fut',
            name='route',
            field=models.CharField(default='treasurer', max_length=50),
        ),
    ]