# Generated by Django 4.2.3 on 2023-07-26 12:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('TrackerApi', '0007_alter_incometracking_user_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incometracking',
            name='user_profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TrackerApi.userprofile'),
        ),
    ]