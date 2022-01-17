from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField
from django.utils.translation import gettext_lazy as _

class ApiDoc(models.Model):
    title = models.CharField(verbose_name= _('Titulo de la API'), max_length=100)
    # img = models.ImageField(upload_to = 'docs/', null = True, blank = True)
    imgURL = models.URLField(max_length=200, null= True, blank= True)
    slug = models.SlugField(editable= False)
    description = models.TextField(verbose_name= _('Descripcion de la API'))

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        super(ApiDoc, self).save(*args, **kwargs)

class ApiDocSection(models.Model):
    api_doc = models.ForeignKey(ApiDoc, on_delete= models.CASCADE, related_name= 'sections')
    api_name = models.CharField(verbose_name= _('Nombre de la API'), max_length= 250)
    api_request = RichTextField(verbose_name= _('Peticion a la API'))
    api_response = RichTextField(verbose_name= _('Respuesta de la API'))
    message = models.TextField(verbose_name= _('Describe algun punto iportante de la API'), null= True, blank= True)

    def __str__(self):
        return f'{self.api_doc.title} {self.api_name}'