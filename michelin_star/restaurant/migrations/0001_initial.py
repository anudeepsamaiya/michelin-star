# Generated by Django 2.1.7 on 2019-03-14 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aggregator_id', models.IntegerField(db_index=True)),
                ('name', models.CharField(db_index=True, max_length=200)),
                ('rating', models.DecimalField(decimal_places=2, max_digits=6, null=True)),
                ('review', models.TextField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]
