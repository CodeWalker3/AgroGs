# Generated by Django 4.1.2 on 2023-02-10 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0009_userprofile_remove_user_profile_pic"),
    ]

    operations = [
        migrations.AlterField(
            model_name="address",
            name="phone",
            field=models.CharField(max_length=100, verbose_name="Phone"),
        ),
        migrations.AlterField(
            model_name="address",
            name="state",
            field=models.CharField(max_length=100, verbose_name="State"),
        ),
        migrations.AlterField(
            model_name="address",
            name="street",
            field=models.CharField(max_length=100, verbose_name="Street"),
        ),
    ]
