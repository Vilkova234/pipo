from django.contrib import admin
from .models import *

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'rating',)
    list_editable = ('rating',)

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    pass


