# Generated by Django 3.0.5 on 2020-07-13 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DrugNotify', '0003_auto_20200609_0350'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='identifier',
            field=models.CharField(default=-1.0, max_length=100, unique=True),
            preserve_default=False,
        ),
    ]
