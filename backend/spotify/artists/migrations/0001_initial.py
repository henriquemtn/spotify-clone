# Generated by Django 4.2.16 on 2024-09-03 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artists',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('banner', models.FileField(blank=True, null=True, upload_to='artists_images/')),
                ('isVerified', models.BooleanField(default=False)),
            ],
        ),
    ]
