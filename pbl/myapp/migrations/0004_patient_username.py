# Generated by Django 4.0.4 on 2022-05-18 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_patient'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='username',
            field=models.CharField(default='mayur', max_length=100),
        ),
    ]