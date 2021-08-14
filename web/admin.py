from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from django.contrib import admin
from .models import *

class CourseLessonsInline(admin.StackedInline):
    model = Lesson
    extra = 0
    verbose_name = 'занятие'
    verbose_name_plural = 'занятия'

class CourseAdmin(admin.ModelAdmin):
    inlines = [CourseLessonsInline]


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name = 'профиль'
    verbose_name_plural = 'профили'

class UserAdmin(BaseUserAdmin):
    inlines = [ProfileInline]


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson)
