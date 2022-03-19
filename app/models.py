import uuid
from django.contrib.auth.models import AbstractUser
from django.db import models




class CourseAddPage(models.Model):
    """Add Course ADMINS"""
    course_name = models.CharField(max_length=255,null=True, blank=True)
    course_price = models.DecimalField(max_digits=7,decimal_places=2,null=True, blank=True)
    course_discount = models.DecimalField(max_digits=7,decimal_places=0,null=True, blank=True)
    image = models.ImageField(upload_to='media/course_pic/',null=True, blank=True)
    course_continu = models.CharField(max_length=255,null=True, blank=True)
    slug = models.SlugField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True,null=True, blank=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.course_name


class CustomerUser(AbstractUser):
    """USER Costumers"""
    USER = (
        (1,'HOD'),
        (2,'STAFF'),
        (3,'STUDENT')
    )
    user_type = models.CharField(choices=USER,max_length=55,default=1)
    profile_pic = models.ImageField(upload_to='media/profile_pic',blank=True,null=True)


class SendRegistr(models.Model):
    """Send Message Register ADMIN"""
    course_name = models.ForeignKey(CourseAddPage,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    is_read = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True,null=True,blank=True)

    def __str__(self):
        return self.name
