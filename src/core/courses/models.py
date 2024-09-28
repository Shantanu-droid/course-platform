from django.db import models

# Create your models here.
def user_directory_path(instance, filename):
    """file will be uploaded to MEDIA_ROOT/user_<id>/<filename>"""
    return f"user_{instance.user.id}/{filename}"

class Courses(models.Model):
    """courses table"""
    class PublishStatus(models.TextChoices):
        """choices class for publish status"""
        PUBLISHED = "publish", "Published"
        DRAFT = "draft", "Draft"
        COMING_SOON = "soon", "Coming Soon"

    class AccessRequirement(models.TextChoices):
        """choices class for access requirement"""
        ANYONE = "any", "Anyone"
        EMAIL_REQUIRED = "email", "Email Required"

    title = models.CharField(max_length=120, )
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(
        upload_to=user_directory_path,
        blank=True,
        null=True
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
