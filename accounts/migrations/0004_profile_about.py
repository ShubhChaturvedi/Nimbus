# Generated by Django 4.1.7 on 2023-03-18 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_profile_options_dob_gender_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='about',
            field=models.TextField(blank=True, max_length=10000, null=True),
        ),
    ]