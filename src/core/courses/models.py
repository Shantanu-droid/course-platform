from django.db import models
from cloudinary.models import CloudinaryField
from helpers import _cloudinary
from utils import slugify

_cloudinary.cloudinary_init()
def user_directory_path(instance, *args, **kwargs): 
    print(args, kwargs)
    if instance.id:
        return f"courses/{instance.id}"
    return "courses"

def get_display_name(instance, *args, **kwargs): 
    print(args, kwargs)
    if instance.title:
        return f"courses/{slugify(instance.title)}"
    return "courses"

class PublishStatus(models.TextChoices):
    """choices class for publish status"""
    PUBLISHED = "publish", "Published"
    DRAFT = "draft", "Draft"
    COMING_SOON = "soon", "Coming Soon"

class Course(models.Model):
    """courses table"""
    class AccessRequirement(models.TextChoices):
        """choices class for access requirement"""
        ANYONE = "any", "Anyone"
        EMAIL_REQUIRED = "email", "Email Required"

    title = models.CharField(max_length=120, )
    description = models.TextField(blank=True, null=True)
    image = CloudinaryField(
        "image",
        blank=True,
        null=True,
        public_id_prefix=user_directory_path
        )
    status = models.CharField(
        max_length=10,
        choices=PublishStatus,
        default=PublishStatus.DRAFT
        )
    access = models.CharField(
        max_length=10,
        choices=AccessRequirement,
        default=AccessRequirement.ANYONE
        )
    
class Lessons(models.Model):
    course = models.ForeignKey(
        Course,
        related_name='lessons',
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=120, )
    description = models.TextField(blank=True, null=True)
    can_preview = models.BooleanField(default=False, help_text='lessons for preview')
    status = models.CharField(
        max_length=10,
        choices=PublishStatus,
        default=PublishStatus.DRAFT
        )
    video = CloudinaryField(
        "video",
        blank=True,
        null=True,
        resource_type='video',
        public_id_prefix=user_directory_path
        )
    custom_order = models.PositiveIntegerField(default=1)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['custom_order', '-updated_at']