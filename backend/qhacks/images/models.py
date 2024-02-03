import uuid
from django.db import models
from storages.backends.s3boto3 import S3Boto3Storage

# Custom storage backend for S3
class S3Storage(S3Boto3Storage):
    location = 'your-s3-bucket-name'

# determine the upload path
def person_image_upload_path(instance, filename):
    # use the person's id (UUID) as the subdirectory
    """
    S3 dir looks like this:
    s3-name/
        |-- person/
        |   |-- 1234-5678/
        |   |   |-- original/
        |   |   |   |-- original_image.jpg
        |   |   |
        |   |   |-- modified/
        |   |       |-- modified_image.jpg
        |-- ...
    """
    return f'person/{instance.id}/{filename}'

class Person(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, null=True, blank=True)
    missing_start = models.DateTimeField()
    currently_missing = models.BooleanField(default=True)

    # Original Image
    original_image = models.ImageField(upload_to=person_image_upload_path, storage=S3Storage(), null=True, blank=True)

    # Modified Image
    modified_image = models.ImageField(upload_to=person_image_upload_path, storage=S3Storage(), null=True, blank=True)

