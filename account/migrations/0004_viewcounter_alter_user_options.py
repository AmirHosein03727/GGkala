# Generated by Django 4.1.7 on 2023-05-14 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_alter_user_email_alter_user_special_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='ViewCounter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_address', models.GenericIPAddressField(verbose_name='آی پی کاربر')),
            ],
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ['-date_joined']},
        ),
    ]