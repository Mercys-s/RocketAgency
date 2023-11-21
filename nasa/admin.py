from django.contrib import admin
from django.utils.safestring import mark_safe

from adminsortable2.admin import SortableAdminMixin

from . import models


@admin.register(models.SliderObject)
class SliderObjectAdmin(SortableAdminMixin, admin.ModelAdmin):

    list_display = ('image_display', 'name', 'my_order')

    def image_display(self, obj):
        return mark_safe(f'<img src="{obj.image.url}"\
                           width = "100" height = "100">')
    
    image_display.short_description = 'Фотография'