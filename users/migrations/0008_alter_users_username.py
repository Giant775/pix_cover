# Generated by Django 5.1 on 2025-03-07 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_orders_users_connections_alter_users_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='username',
            field=models.CharField(default='lkVWffOguMNF3eRUgItLq9SFShrerEzwZ6MVkNBDUsFxdnDTbS', max_length=20, unique=True),
        ),
    ]
