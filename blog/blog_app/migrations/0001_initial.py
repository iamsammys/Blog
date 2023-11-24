# Generated by Django 4.2.5 on 2023-10-29 12:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.CharField(max_length=200, primary_key=True, serialize=False, unique=True)),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
                ('title', models.CharField(max_length=100, null=True)),
                ('content', models.TextField(null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
