# Generated by Django 4.2.3 on 2023-07-24 16:20

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('TrackerApi', '0005_remove_expensetracking_income_incometracking_income_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='incometracking',
            name='income',
        ),
        migrations.AddField(
            model_name='expensetracking',
            name='income',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='TrackerApi.incometracking'),
            preserve_default=False,
        ),
    ]