from django.contrib import admin
from rango.models import Category, Page

# admin.site.register(Category)
# admin.site.register(Page)

class PageAdmin(admin.ModelAdmin):
    list_display = ('title','category','url')

admin.site.register(Page, PageAdmin)


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('name',)}

admin.site.register(Category, CategoryAdmin)


"""
class PageInline(admin.TabularInline):
    model = Page
    extra = 1

class CategoryAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['name']}),
        ('Viewing information', {'fields': ['views', 'likes']}),
    ]
    inlines = [PageInline]
    
"""



