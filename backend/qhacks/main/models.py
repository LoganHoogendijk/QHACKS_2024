import uuid
from django.db import models
from storages.backends.s3boto3 import S3Boto3Storage
from django.contrib.auth.models import User
from django.conf import settings

# Custom storage backend for S3
class S3Storage(S3Boto3Storage):
    location = settings.AWS_STORAGE_BUCKET_NAME

# determine the upload path
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
    crop_id = instance.crops.first().id
    return f'person/{crop_id}/{filename}'

class UserProfile(models.Model):
    # has username and password from the user model
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    id = models.UUIDField(default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    crops = models.ManyToManyField('Crop', related_name='users', blank=True)

class Crop(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    label = models.CharField(max_length=100)
    leaves = models.ManyToManyField('Leaf', related_name='crops', blank=True)
    crop_type = models.CharField(max_length=100)

class Leaf(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    image = models.ImageField(upload_to=leaf_image_upload_path, storage=S3Storage(), null=True, blank=True)
    time_stamp = models.DateTimeField(auto_now_add=True)
    recommendations = models.ManyToManyField('Recommendation', related_name='leaves')

class Recommendation(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    content = models.CharField(max_length=500)
    complete = models.BooleanField(default=False)
