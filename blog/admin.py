from django.contrib import admin
from .models import Post, Tag, Comment
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields={"slug": ("title",)}
    list_display = ["title", "published_at"]

admin.site.register(Post, PostAdmin)
admin.site.register(Tag)
admin.site.register(Comment)