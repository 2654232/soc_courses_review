
# Register your models here.
from django.contrib import admin
from reviewer.models import Course, Review

# Register your models here.

class ReviewAdmin(admin.ModelAdmin):
     list_display = ('Course','Rating', 'comment')

class CourseAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('Name',)}

admin.site.register(Course,CourseAdmin)
admin.site.register(Review,ReviewAdmin)



