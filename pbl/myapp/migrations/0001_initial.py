# Generated by Django 4.0.4 on 2022-05-08 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=100)),
                ('lname', models.CharField(max_length=100)),
                ('pnumber', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=100)),
                ('password', models.CharField(max_length=10)),
            ],
        ),
    ]
