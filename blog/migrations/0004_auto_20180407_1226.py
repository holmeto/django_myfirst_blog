# Generated by Django 2.0.1 on 2018-04-07 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20180406_1625'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='author',
        ),
        migrations.AlterField(
            model_name='blog',
            name='content',
            field=models.TextField(default='', verbose_name='内容'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='tag',
            field=models.ManyToManyField(default='', to='blog.Tag', verbose_name='标签'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='title',
            field=models.CharField(default='', max_length=60, verbose_name='博客标题'),
        ),
    ]
