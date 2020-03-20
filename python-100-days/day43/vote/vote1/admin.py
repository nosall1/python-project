from django import forms
from django.contrib import admin
from vote1.models import Subject,Teacher,User
from vote1.form import UserForm
# Register your models here.
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('no','name','create_date','is_hot')
    ordering = ('no',)

class TeacherAdmin(admin.ModelAdmin):
    list_display = ('no','name','detail','good_count','bad_count','subject')
    ordering = ('subject','no')

admin.site.register(Subject,SubjectAdmin)
admin.site.register(Teacher, TeacherAdmin)




class UserAdmin(admin.ModelAdmin):
    list_display = ('no', 'username', 'password')
    ordering = ('no', )
    form = UserForm
    list_per_page = 10


admin.site.register(User, UserAdmin)