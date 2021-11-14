from django.contrib import admin
from django.contrib.admin.sites import site

# Register your models here.
from .models import Link, SideBar

@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    pass

@admin.register(SideBar)
class SideBarAdmin(admin.ModelAdmin):
    pass