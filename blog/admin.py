from django.contrib import admin
from blog.models import BlogItem, BlogSetting
# Register your models here.
admin.site.register(BlogItem)
admin.site.register(BlogSetting)
