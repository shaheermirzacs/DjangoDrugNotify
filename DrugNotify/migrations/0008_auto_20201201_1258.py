# Generated by Django 3.0.5 on 2020-12-01 12:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('DrugNotify', '0007_auto_20201201_1238'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='test',
            name='user',
        ),
        migrations.AddField(
            model_name='test',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='DrugNotify.User'),
        ),
    ]