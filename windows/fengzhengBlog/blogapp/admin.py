from django.contrib import admin
from fengzhengBlog.blogapp.models import *

# Register your models here.
class article_admin(admin.ModelAdmin):
    list_display = ("title","content","author","ispublished")
    search_fields = ("title","author")
    list_filter = ("author",'publish_date')
    date_hierarchy = "publish_date"
    #fields = ("title","content","author","ispublished",'publish_date','commentcount','readcount')
    raw_id_fields = ("author",)

admin.site.register(fz_user)
admin.site.register(fz_Article,article_admin)
admin.site.register(fz_comment)
admin.site.register(fz_classic)