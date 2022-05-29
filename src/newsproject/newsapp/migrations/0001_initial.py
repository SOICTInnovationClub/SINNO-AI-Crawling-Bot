# Generated by Django 4.0.4 on 2022-05-29 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewsArticle',
            fields=[
                ('title', models.CharField(max_length=200)),
                ('url', models.URLField(primary_key=True, serialize=False)),
                ('body', models.TextField(blank=True, null=True)),
                ('top_image', models.URLField(blank=True, null=True)),
                ('pub_date', models.DateTimeField(blank=True, null=True)),
                ('summary', models.TextField(blank=True, null=True)),
                ('publisher', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
