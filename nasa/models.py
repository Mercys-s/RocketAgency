from django.db import models

from filer.fields.image import FilerImageField


class SliderObject(models.Model):
    name = models.CharField(max_length = 70, db_index = True, verbose_name = 'Имя фотографии')
    image = FilerImageField(blank = False, on_delete = models.CASCADE, verbose_name = 'Фотография')
    my_order = models.PositiveIntegerField(default = 0, blank = False, null = False)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Объекты слайдера'
        ordering = ['my_order']
