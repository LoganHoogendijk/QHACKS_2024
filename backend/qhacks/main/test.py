from .resnet9 import ResNet9, classes
from .predict import ImageClassifier
from django.core.files.storage import default_storage
from django.conf import settings
import os
import boto3
from django.conf import settings

def get_model_results(url):
    # AWS credentials and region
    aws_access_key_id = settings.AWS_ACCESS_KEY_ID
    aws_secret_access_key = settings.AWS_SECRET_ACCESS_KEY
    region_name = settings.AWS_S3_REGION_NAME

    # S3 bucket and key (object key)
    bucket_name = 'qhacks2024'
    start_index = url.find('.com') + len('.com')
    end_index = url.find('?')

    object_key = url[start_index + 1:end_index]
    # Local file path to save the downloaded image
    base_dir =settings.MEDIA_ROOT
    local_file_path = os.path.join(base_dir, "tmp.jpg")

    # Create an S3 client
    s3 = boto3.client('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key, region_name=region_name)

    # Download the file from S3 and save it locally
    # local_file_path = default_storage.path('tmp.jpg')
    s3.download_file(bucket_name, object_key, local_file_path)

    # Now you can use the local file for further processing
    result_dict = ImageClassifier().result_dict(local_file_path)

    # To clear the file
    open("./media/tmp.jpg", 'wb').close()
    return result_dict

