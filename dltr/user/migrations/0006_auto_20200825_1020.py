# Generated by Django 3.1 on 2020-08-25 02:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_auto_20200825_1014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='uid',
            field=models.CharField(default='', max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_name',
            field=models.CharField(default='', max_length=20),
        ),
    ]
