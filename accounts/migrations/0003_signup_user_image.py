# Generated by Django 3.2.4 on 2021-07-08 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_remove_signup_user_passwordre'),
    ]

    operations = [
        migrations.AddField(
            model_name='signup_user',
            name='image',
            field=models.ImageField(default='', upload_to='profile/image'),
        ),
    ]
