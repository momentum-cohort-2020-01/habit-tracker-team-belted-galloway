# Generated by Django 3.0.4 on 2020-03-08 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20200306_2010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habit',
            name='goal_unit',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='dailylog',
            unique_together={('habit', 'activity_date')},
        ),
    ]