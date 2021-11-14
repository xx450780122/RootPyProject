from typing import List
from django.contrib import admin
from django.contrib.admin import actions
from django.utils.html import format_html
from django.urls import reverse

# Register your models here.
from .models import Post,Category, Tag
from fiveclass.custom_site import customsite

@admin.register(Post,site=customsite)
class PostAdmin(admin.ModelAdmin):
    list_display = [
    'title','category','status',
    'owner','created_time','operator'
    ]
    #list_display_links = ['title','category','status']
    list_filter = ('category','owner') 
    search_fields = ['title','category__name','owner__username']
    
    save_on_top = True
    actions_on_top = True
    #actions_on_bottom = True
    date_hierarchy = 'created_time'
    list_editable=[]
    
    def operator(selef,obj):
        return format_html(
            '<a href="{}">编辑</a>',
            reverse('cus_admin:blog_post_change',args=(obj.id,))
        )
    operator.allow_tags = True
    operator.short_description = '操作'
    

@admin.register(Category,site=customsite)
class CategoroyAdmin(admin.ModelAdmin):
    pass

@admin.register(Tag,site=customsite)
class TagAdmin(admin.ModelAdmin):
    pass

