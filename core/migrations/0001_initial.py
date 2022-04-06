# Generated by Django 3.1.2 on 2022-04-05 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='githubRepos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('language', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField()),
                ('html_url', models.URLField()),
            ],
        ),
    ]
