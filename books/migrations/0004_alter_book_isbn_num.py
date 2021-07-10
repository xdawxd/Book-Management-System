# Generated by Django 3.2.5 on 2021-07-09 23:26

from django.db import migrations
import isbn_field.fields
import isbn_field.validators


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_alter_book_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='isbn_num',
            field=isbn_field.fields.ISBNField(max_length=28, validators=[isbn_field.validators.ISBNValidator], verbose_name='ISBN'),
        ),
    ]