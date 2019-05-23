# Generated by Django 2.2.1 on 2019-05-23 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField(db_index=True)),
                ('date_pub', models.DateTimeField(auto_now_add=True)),
                ('author', models.CharField(max_length=30)),
            ],
        ),
    ]
