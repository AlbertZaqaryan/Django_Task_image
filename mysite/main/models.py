from django.db import models

# Create your models here.


class Shoes(models.Model):

    name = models.CharField('Shoes name', max_length=60)
    price = models.PositiveIntegerField('Shoes price')
    img = models.ImageField('Shoes image', upload_to='images')
    date = models.DateTimeField('Shoes create date', auto_now=True)
    about = models.TextField('Shoes about')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Shoes'
        verbose_name_plural = 'Shoes'
        ordering = ['date']
    