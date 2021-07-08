# Generated by Django 3.2.4 on 2021-07-07 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobhunter', '0005_alter_posting_responsibilities'),
    ]

    operations = [
        migrations.RenameField(
            model_name='posting',
            old_name='posting_due_date',
            new_name='due_date',
        ),
        migrations.RenameField(
            model_name='posting',
            old_name='position_level',
            new_name='level',
        ),
        migrations.RenameField(
            model_name='posting',
            old_name='position_type',
            new_name='type',
        ),
        migrations.RenameField(
            model_name='posting',
            old_name='posting_url',
            new_name='url',
        ),
        migrations.AlterField(
            model_name='posting',
            name='other',
            field=models.CharField(max_length=256),
        ),
    ]