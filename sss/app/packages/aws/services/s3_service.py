import uuid
from typing import IO, Any, Literal, TypeAlias

import boto3
import requests
from django.conf import settings

TContentTypes: TypeAlias = Literal["image/jpg", "image/jpeg", "image/png", "video/mp4"]

client = boto3.client(
    service_name="s3",
    region_name=settings.AWS_REGION_NAME,
    aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
    aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
)


def upload(
    *,
    filebytes: IO[Any],
    filename: str,
    content_type: TContentTypes,
) -> str:
    s3_key = f"{str(uuid.uuid4())}/{filename}"
    client.upload_fileobj(
        Fileobj=filebytes,
        Bucket="flit",
        Key=s3_key,
        ExtraArgs={"ContentType": content_type, "ACL": "public-read"},
    )
    return _create_url(s3_key)


def upload_from_url(*, url: str, filename: str, content_type: TContentTypes) -> str:
    response = requests.get(url, stream=True)
    return upload(filebytes=response.raw, filename=filename, content_type=content_type)


def upload_from_path(*, path: str, filename: str, content_type: TContentTypes) -> str:
    s3_key = f"{str(uuid.uuid4())}/{filename}"
    client.upload_file(
        Filename=path,
        Bucket="flit",
        Key=s3_key,
        ExtraArgs={"ContentType": content_type, "ACL": "public-read"},
    )
    return _create_url(s3_key)


def _create_url(s3_key: str):
    return f"https://flit.s3.{settings.AWS_REGION_NAME}.amazonaws.com/{s3_key}"
