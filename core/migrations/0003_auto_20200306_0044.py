# Generated by Django 3.0.4 on 2020-03-06 00:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0002_auto_20200305_2316'),
    ]

    operations = [
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.AlterModelOptions(
            name='habit',
            options={'ordering': ['-created_at']},
        ),
        migrations.AddField(
            model_name='habit',
            name='goal_value',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='habit',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='users_habits', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='habit',
            name='goal_unit',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Unit'),
        ),
    ]
