import uuid
from django.db import models
from storages.backends.s3boto3 import S3Boto3Storage
from django.contrib.auth.models import User
from django.conf import settings

# Custom storage backend for S3
class S3Storage(S3Boto3Storage):
    location = settings.AWS_STORAGE_BUCKET_NAME

def leaf_image_upload_path(instance, filename):
    # use the crop's id (UUID) as the subdirectory
    """
    S3 dir looks like this:
    s3-name/
        |   |-- 1234-5678 (crop id)/
        |   |   |-- leaf1.jpg
                |-- leaf2.jpg
        |   |-- ...
    """
    return f'leaves/{instance.id}/{filename}'

class UserProfile(models.Model):
    # has username and password from the user model
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    crops = models.ManyToManyField('Crop', related_name='users', blank=True)

class Crop(models.Model):
    label = models.CharField(max_length=100)
    leaves = models.ManyToManyField('Leaf', related_name='crops', blank=True)
    crop_type = models.CharField(max_length=100)

class Leaf(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    image = models.ImageField(upload_to=leaf_image_upload_path, storage=S3Storage(), null=True, blank=True)
    time_stamp = models.DateTimeField(auto_now_add=True)
    recommendations = models.ManyToManyField('Recommendation', related_name='leaves', blank=True)
    # crop = models.ForeignKey('Crop', on_delete=models.CASCADE, related_name='leaves')

class Recommendation(models.Model):
    content = models.CharField(max_length=1500)
    complete = models.BooleanField(default=False)
