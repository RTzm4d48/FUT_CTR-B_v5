# Generated by Django 4.2 on 2023-05-09 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp_admin', '0002_alter_admins_dni_alter_admins_email_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='process',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tittle', models.CharField(max_length=40)),
                ('name', models.CharField(max_length=40)),
                ('reception', models.DateTimeField()),
                ('exit', models.DateTimeField()),
                ('state', models.BooleanField()),
                ('num', models.IntegerField()),
            ],
        ),
    ]