from django.contrib import admin

from blog.models import *


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
'''
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)

'''

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title','category','content','pub_time','id','user','user_id',)



class CommentAdmin(admin.ModelAdmin):
    list_display = ('blog','name','content','pub')

class UserAdmin(admin.ModelAdmin):
    list_display = ('username','id')

admin.site.register(Category,CategoryAdmin)
#admin.site.register(Tag,TagAdmin)
admin.site.register(Blog,BlogAdmin)
admin.site.register(Comment,CommentAdmin)
admin.site.register(User,UserAdmin)


# Register your models here.
