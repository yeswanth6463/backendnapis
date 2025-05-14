from django.contrib import admin
from .models import student,teacher,course,course_category,Common_user,course_video,Chapter
# Register your models here.
admin.site.register(student)
admin.site.register(teacher)
admin.site.register(course_category)
admin.site.register(course)
admin.site.register(Chapter)
admin.site.register(course_video)
admin.site.register(Common_user)
admin.site.site_header = "Scopick Admin Portal"
admin.site.site_title = "Scopick Admin Portal"
admin.site.index_title = "Welcome to Scopick Admin Portal"
admin.site.site_url = "/admin/"

#how to change site icon'








# how to deeign the admin panel
# admin.site.index_template = "admin/index.html"
# admin.site.index_template = "admin/index.html"
admin.site.index_template = "admin/index.html"








