from django.contrib import admin
from .models import Flat,FlatImage


class FlatImageInline(admin.TabularInline):
    model = FlatImage
    extra = 3

class FlatAdmin(admin.ModelAdmin):
    inlines = [ FlatImageInline, ]

admin.site.register(Flat, FlatAdmin)