# Generated by Django 4.2.11 on 2024-06-16 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0002_alter_customuser_is_approved"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="is_active",
            field=models.BooleanField(default=True),
        ),
    ]
