from django.contrib import admin

# Register your models here.
from .models import *


class PostAdmin(admin.ModelAdmin):
    #list_display = '__all__'
    list_display=('title','body','image','slug','updated','timestamp')
    list_filter = ('updated','timestamp')
    list_display_links = ('updated',)
    list_editable = ('title',)
    prepopulated_fields= {'slug':['title']} # this is for slug ...like slug.js file for create post

   # class Meta:
   #     model=Post

admin.site.register(Post,PostAdmin)




class ContactAdmin(admin.ModelAdmin):
    list_display = ('name','email','comments')
    list_filter = ('name',)

admin.site.register(Contact,ContactAdmin)





admin.site.site_header='BlogLog'
