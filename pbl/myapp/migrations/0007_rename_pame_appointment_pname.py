# Generated by Django 4.0.4 on 2022-05-29 17:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_appointment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appointment',
            old_name='pame',
            new_name='pname',
        ),
    ]
