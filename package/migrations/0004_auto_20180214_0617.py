# Generated by Django 1.11.10 on 2018-02-14 06:17

from django.db import migrations, models
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('package', '0003_packageexample_created_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='created',
            field=django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created'),
        ),
        migrations.AlterField(
            model_name='category',
            name='modified',
            field=django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified'),
        ),
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(max_length=50, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='category',
            name='title_plural',
            field=models.CharField(blank=True, max_length=50, verbose_name='Title Plural'),
        ),
        migrations.AlterField(
            model_name='commit',
            name='created',
            field=django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created'),
        ),
        migrations.AlterField(
            model_name='commit',
            name='modified',
            field=django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified'),
        ),
        migrations.AlterField(
            model_name='package',
            name='created',
            field=django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created'),
        ),
        migrations.AlterField(
            model_name='package',
            name='modified',
            field=django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified'),
        ),
        migrations.AlterField(
            model_name='package',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='packageexample',
            name='created',
            field=django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created'),
        ),
        migrations.AlterField(
            model_name='packageexample',
            name='modified',
            field=django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified'),
        ),
        migrations.AlterField(
            model_name='packageexample',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='version',
            name='created',
            field=django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created'),
        ),
        migrations.AlterField(
            model_name='version',
            name='license',
            field=models.CharField(max_length=100, verbose_name='license'),
        ),
        migrations.AlterField(
            model_name='version',
            name='modified',
            field=django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified'),
        ),
        migrations.AlterField(
            model_name='version',
            name='number',
            field=models.CharField(blank='', default='', max_length=100, verbose_name='Version'),
        ),
    ]
