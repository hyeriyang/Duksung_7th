# Generated by Django 2.2.1 on 2019-05-24 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notice', '0003_merge_20190524_1042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notice',
            name='file',
            field=models.FileField(null=True, upload_to='document/'),
        ),
    ]
