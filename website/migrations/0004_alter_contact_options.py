# Generated by Django 4.2 on 2024-12-17 23:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_alter_contact_id'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contact',
            options={'ordering': ['-creatade_date']},
        ),
    ]
