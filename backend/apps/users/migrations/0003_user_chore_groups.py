# Generated by Django 3.2.15 on 2022-10-02 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chores', '0003_many_to_many_group_page'),
        ('users', '0002_alter_user_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='chore_groups',
            field=models.ManyToManyField(related_name='watchers', to='chores.ChoreGroup'),
        ),
    ]
