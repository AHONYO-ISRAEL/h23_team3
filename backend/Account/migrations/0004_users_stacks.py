# Generated by Django 4.2 on 2023-10-22 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0003_alter_stacks_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='stacks',
            field=models.ManyToManyField(related_name='users_stacks', to='Account.userstacks'),
        ),
    ]
