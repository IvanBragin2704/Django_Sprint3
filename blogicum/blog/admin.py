from django.contrib import admin

from .models import Category, Post, Location

admin.site.empty_value_display = 'Не задано'


class LocationAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_published']
    list_editable = ['is_published']
    search_fields = ['name']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_published']
    list_editable = ['is_published']
    search_fields = ['title']
    prepopulated_fields = {'slug': ['title']}


class PostAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'pub_date',
        'author',
        'category',
        'is_published',
        'location'
    ]
    list_editable = [
        'is_published',
        'category',
        'location'
    ]
    search_fields = ['title', 'text']
    list_filter = ['category', 'is_published', 'pub_date']
    list_display_links = ['title']
    filter_horizontal = []


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Location)
