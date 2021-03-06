from django.db import models
from django.core.validators import MinValueValidator, MinLengthValidator
from isbn_field import ISBNField
# Create your models here.

# TODO -> create an author model since one book can have multiple authors, use many to many relationship


class Book(models.Model):
    title = models.CharField('Title', max_length=200, validators=[MinLengthValidator(2)])
    author = models.CharField('Author', max_length=100, validators=[MinLengthValidator(2)])
    pub_date = models.DateField('Publication Date')
    isbn_num = ISBNField('ISBN')
    page_count = models.IntegerField('Number of Pages', validators=[MinValueValidator(1)], blank=True, null=True)
    language = models.CharField('Language', max_length=4, validators=[MinLengthValidator(2)])
    preview_link = models.URLField('Preview')

    def __str__(self):
        return self.title
