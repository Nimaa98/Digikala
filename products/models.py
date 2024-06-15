from django.db import models
from django.utils.translation import  gettext as _

# Create your models here.

class Product(models.Model):
    name = models.CharField(_('Persian Name'),max_length=200)
    en_name = models.CharField(_('English Name'),max_length=200)
    description = models.TextField(_('Description'))
    category = models.ForeignKey('Category',
                                verbose_name = _('Category'),
                                on_delete = models.RESTRICT
                                )




    def __str__(self):
        return f'{self.id}  {self.name}'



class Category(models.Model):
    name = models.CharField(_('Name'),max_length=50)
    slug = models.SlugField(_('Slug'))
    description = models.TextField(_('Description'))
    icon = models.ImageField(_('Icon'),upload_to='category_images')
    image = models.ImageField(_('Image'),upload_to='category_images')
