# Generated by Django 3.2.4 on 2021-06-12 00:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sinistros', '0003_auto_20210611_2110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='violacao',
            name='bo',
            field=models.FileField(blank=True, null=True, upload_to='uploads/%Y/%m/%d', verbose_name='Relatório do Sistema'),
        ),
        migrations.AlterField(
            model_name='violacao',
            name='cliente',
            field=models.CharField(default=1, max_length=30, verbose_name='Cliente'),
            preserve_default=False,
        ),
    ]
