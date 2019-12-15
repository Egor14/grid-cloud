# Generated by Django 3.0 on 2019-12-14 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('worker', '0002_auto_20191207_2029'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='input_data',
            new_name='link',
        ),
        migrations.RemoveField(
            model_name='task',
            name='type',
        ),
        migrations.AddField(
            model_name='task',
            name='bytes',
            field=models.BinaryField(default=b's', max_length=10000000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='task',
            name='image',
            field=models.ImageField(default='s', upload_to=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='task',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]