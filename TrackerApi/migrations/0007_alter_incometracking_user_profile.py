# Generated by Django 4.2.3 on 2023-07-26 11:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('TrackerApi', '0006_remove_incometracking_income_expensetracking_income'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incometracking',
            name='user_profile',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='TrackerApi.userprofile'),
        ),
    ]
