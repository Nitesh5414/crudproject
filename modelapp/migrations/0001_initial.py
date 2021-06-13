# Generated by Django 3.1.7 on 2021-04-15 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('marks', models.FloatField()),
                ('roll_num', models.IntegerField()),
            ],
        ),
    ]
