from django.contrib import admin

# Register your models here.
from .models import Post,Category, Tag

class PostAdmin(admin.ModelAdmin):
    pass

class CategoroyAdmin(admin.ModelAdmin):
    pass

class TagAdmin(admin.ModelAdmin):
    pass

admin.site.register(Post)
admin.site.register(Tag)
admin.site.register(Category)