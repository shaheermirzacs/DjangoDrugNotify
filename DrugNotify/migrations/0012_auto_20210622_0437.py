# Generated by Django 3.2.4 on 2021-06-22 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DrugNotify', '0011_test_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='first_name',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='test',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]