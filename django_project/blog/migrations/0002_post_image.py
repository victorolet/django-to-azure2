# Generated by Django 2.2.6 on 2019-12-09 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='Image',
            field=models.ImageField(default='default.jpg', upload_to='post_pics'),
        ),
    ]
