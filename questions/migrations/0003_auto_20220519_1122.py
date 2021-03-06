# Generated by Django 3.2.12 on 2022-05-19 11:22

from django.db import migrations, models
import markupfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0002_auto_20220519_0636'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='_body_rendered',
            field=models.TextField(editable=False, null=True),
        ),
        migrations.AddField(
            model_name='content',
            name='body_markup_type',
            field=models.CharField(choices=[('', '--'), ('html', 'HTML'), ('plain', 'Plain')], default='html', max_length=30),
        ),
        migrations.AlterField(
            model_name='content',
            name='body',
            field=markupfield.fields.MarkupField(null=True, rendered_field=True),
        ),
    ]
