from django.contrib import admin
from .models import PageLinks

@admin.register(PageLinks)
class PageLinksAdmin(admin.ModelAdmin):
    list_display = ("ipo_url", "rne_url")
