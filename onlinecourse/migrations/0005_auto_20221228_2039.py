# Generated by Django 3.1.3 on 2022-12-28 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecourse', '0004_auto_20221228_1952'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='submission',
            name='pub_date',
        ),
        migrations.AlterField(
            model_name='choice',
            name='choice_text',
            field=models.CharField(default='enter choice text', max_length=400),
        ),
    ]
