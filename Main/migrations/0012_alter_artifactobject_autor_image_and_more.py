# Generated by Django 4.2.5 on 2023-10-31 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0011_remove_artifactobject_main_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artifactobject',
            name='autor_image',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='artifactobject',
            name='name_image',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='artifactobject',
            name='path_image',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='artifactobject',
            name='sourc_image',
            field=models.CharField(max_length=100),
        ),
    ]