# Generated by Django 3.1 on 2020-11-06 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20201106_1119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicacion',
            name='titulo',
            field=models.CharField(max_length=100),
        ),
    ]
