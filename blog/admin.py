from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'fecha_publicacion')  # columnas en la tabla
    search_fields = ('titulo',)
    ordering = ('-fecha_publicacion',)