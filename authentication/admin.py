from django.contrib import admin
from .models import Post,PostImage
from django.utils.html import format_html

# class PostImageInline(admin.TabularInline):
#     model=PostImage
#     extra=3

class PostImageInline(admin.TabularInline):

    model=PostImage
    readonly_fields=['thumbnail']

    def thumbnail(self,instance):
        if instance.image.name!='':
            return format_html(f"<img src='{instance.image.url}' class='thumbnail'/>")                     
        return ""


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display=['id','title','description','created_at','display_image']
    inlines=[PostImageInline]
    autocomplete_fields=['user']
    # list_select_related=['image']

    def display_image(self,post):
        return post.image 



    class Media:
        css={
            'all':['style.css']
        }

    
