# Generated by Django 3.0.4 on 2020-03-06 17:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20200306_0044'),
    ]

    operations = [
        migrations.RenameField(
            model_name='habit',
            old_name='habit',
            new_name='name',
        ),
    ]