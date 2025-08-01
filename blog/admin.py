from django.contrib import admin

from .models import Post, Author, Tag

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_filter = ('title', 'author', 'tags')
    list_display = ('title', 'excerpt')
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Post, PostAdmin)
admin.site.register(Author)
admin.site.register(Tag)
