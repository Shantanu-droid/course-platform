from .models import Course

def get_image_thumbnail(course: Course, as_html=False, width=200):
        if not course.image:
            return ""
        image_options = {
            'width':width
        }
        if as_html:
            # CloudinaryImage(str(instance.image)).image(width=width)
            return course.image.image(**image_options)
        url = course.image.build_url()
        return url