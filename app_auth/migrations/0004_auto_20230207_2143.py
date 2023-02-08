# Generated by Django 3.2 on 2023-02-07 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_auth', '0003_auto_20230201_0020'),
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.PositiveSmallIntegerField(choices=[(1, 'student'), (2, 'teacher'), (3, 'secretary'), (4, 'supervisor'), (5, 'admin')], primary_key=True, serialize=False)),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='roles',
            field=models.ManyToManyField(to='app_auth.Role'),
        ),
    ]
