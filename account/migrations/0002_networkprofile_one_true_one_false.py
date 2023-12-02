# Generated by Django 4.2.7 on 2023-12-01 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='networkprofile',
            constraint=models.CheckConstraint(check=models.Q(models.Q(('customer', False), ('networkAdmin', True)), models.Q(('customer', True), ('networkAdmin', False)), _connector='OR'), name='one_true_one_false'),
        ),
    ]
