# Generated by Django 4.2 on 2023-05-05 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admins',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('fullname', models.TextField()),
                ('email', models.TextField()),
                ('position', models.TextField()),
                ('phone', models.TextField()),
                ('dni', models.TextField()),
                ('password', models.TextField()),
            ],
        ),
    ]