from django.core.files.uploadedfile import InMemoryUploadedFile, TemporaryUploadedFile
from django.http import HttpRequest, HttpResponse

from sss.app.models import FileAttachment
from sss.app.packages.aws.services import s3_service
from sss.app.routes.decorator import route
from sss.app.viewsets.base.base_api_view import APIView

__all__ = ["VideoUploadAPIView"]


@route("video")
class VideoUploadAPIView(APIView):
    def post(self, request: HttpRequest):
        files = request.FILES
        for _, file in files.items():
            if isinstance(file, TemporaryUploadedFile):
                link = s3_service.upload_from_path(
                    path=file.temporary_file_path(),
                    filename=file.name,
                    content_type=file.content_type,  # type: ignore
                )
            elif isinstance(file, InMemoryUploadedFile):
                link = s3_service.upload(
                    filebytes=file.open(),
                    filename=file.name,
                    content_type=file.content_type,  # type: ignore
                )
            else:
                raise Exception("never")

            FileAttachment.objects.create(
                content_type=file.content_type,
                link=link,
                name=file.name,
                size=file.size,
            )
        return HttpResponse()
