from django.contrib import admin
from .models import CourseAddPage,SendRegistr



class CourseAdmin(admin.ModelAdmin):
    model = CourseAddPage
    list_display = ['course_name','course_price','course_discount']
    list_editable = ['course_price','course_discount']

admin.site.register(CourseAddPage,CourseAdmin)
admin.site.register(SendRegistr)
