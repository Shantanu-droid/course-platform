from cloudinary import CloudinaryImage

from django.contrib import admin
from django.utils.html import format_html
from .models import Course, Lessons
from .services import get_image_thumbnail


# Register your models here.
class LessonInline(admin.StackedInline):
    model = Lessons
    extra = 0
    
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    fields=['title', 'description', 'status', 'image', 'display_image', 'access']
    readonly_fields = ['display_image']
    inlines = [LessonInline]

    def display_image(self, instance):
        return format_html(get_image_thumbnail(instance, as_html=True, width=200))
    
    display_image.short_description = 'Current Image'
