# Generated by Django 4.2.5 on 2023-10-07 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0002_image_remove_arhetectureobject_img_autor_1_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='arhetectureobject',
            name='type_build',
            field=models.CharField(choices=[('v1', 'Замок'), ('v2', 'Ратуша'), ('v2', 'Православный храм'), ('v3', 'Католический храм'), ('v4', 'Синагога'), ('v5', 'Дворец/Усадьба'), ('v6', 'Разное')], default='Замок', max_length=50),
        ),
    ]