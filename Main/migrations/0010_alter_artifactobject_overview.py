# Generated by Django 4.2.5 on 2023-10-10 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0009_alter_artifactobject_overview'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artifactobject',
            name='overview',
            field=models.TextField(),
        ),
    ]