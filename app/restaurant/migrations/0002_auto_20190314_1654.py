# Generated by Django 2.1.7 on 2019-03-14 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='name',
            field=models.CharField(blank=True, db_index=True, max_length=200),
        ),
    ]
