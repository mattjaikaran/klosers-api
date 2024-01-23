# from rest_framework.views import exception_handler
# from django.conf import settings
# from storages.backends.s3boto3 import S3Boto3Storage
# from boto3 import Session


# class PublicMediaStorage(S3Boto3Storage):
#     location = settings.DEFAULT_FILE_STORAGE
#     default_acl = "public-read"
#     file_overwrite = False
#     custom_domain = False

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.session = Session(
#             aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
#             aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
#             region_name=settings.AWS_S3_REGION_NAME,
#         )

#     def url(self, name):
#         url = super().url(name)
#         if self.custom_domain:
#             return url
#         return self.session.client("s3").generate_presigned_url(
#             "get_object", Params={"Bucket": self.bucket.name, "Key": name}
#         )


# class PrivateMediaStorage(S3Boto3Storage):
#     location = settings.PRIVATE_MEDIAFILES_LOCATION
#     default_acl = "private"
#     file_overwrite = False
#     custom_domain = False

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.session = Session(
#             aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
#             aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
#             region_name=settings.AWS_S3_REGION_NAME,
#         )

#     def url(self, name):
#         url = super().url(name)
#         if self.custom_domain:
#             return url
#         return self.session.client("s3").generate_presigned_url(
#             "get_object", Params={"Bucket": self.bucket.name, "Key": name}
#         )


# def custom_exception_handler(exc, context):
#     response = exception_handler(exc, context)
#     if response is not None:
#         response.data["status_code"] = response.status_code
#     return response
