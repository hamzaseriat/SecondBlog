from django.contrib import admin
from .models import Blogs , Category
from django.utils.safestring import mark_safe
# Register your models here.

class Blogadmin(admin.ModelAdmin):
    list_display = ("title","is_active","is_home","selected_categories")
    list_editable = ("is_active","is_home")
    search_fields = ("title","description")
    readonly_fields = ("slug",)
    list_filter = ("is_active","is_home")
    
    def selected_categories(self,obj):
        html = "<ul>"
        for category in obj.category.all():
            html += "<li>" + category.categories + "</li>"
            
        html += "</ul>"
        return mark_safe(html)
       
       
class Categoryadmin(admin.ModelAdmin):
    readonly_fields = ("slug",)
    
    
    
admin.site.register(Blogs,Blogadmin)
admin.site.register(Category,Categoryadmin)
