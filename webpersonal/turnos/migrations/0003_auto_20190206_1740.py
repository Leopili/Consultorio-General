# Generated by Django 2.0 on 2019-02-06 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('turnos', '0002_profesional'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profesional',
            options={'verbose_name': 'Profesional\t', 'verbose_name_plural': 'Profesionales'},
        ),
        migrations.AddField(
            model_name='profesional',
            name='especialidad',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
    ]
