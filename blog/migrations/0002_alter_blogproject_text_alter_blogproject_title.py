# Generated by Django 4.1.7 on 2023-05-02 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogproject',
            name='text',
            field=models.TextField(max_length=3000),
        ),
        migrations.AlterField(
            model_name='blogproject',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]
