# Generated by Django 3.0.5 on 2020-07-13 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DrugNotify', '0004_user_identifier'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='id',
        ),
        migrations.AlterField(
            model_name='user',
            name='identifier',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
    ]
