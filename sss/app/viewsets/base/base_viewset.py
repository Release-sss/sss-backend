from django.http import HttpRequest
from djangorestframework_camel_case.parser import CamelCaseJSONParser
from djangorestframework_camel_case.render import CamelCaseJSONRenderer
from rest_framework.viewsets import ModelViewSet as _ModelViewSet

__all__ = ["ModelViewSet"]


class ModelViewSet(_ModelViewSet):

    renderer_classes = [CamelCaseJSONRenderer]
    parser_classes = [CamelCaseJSONParser]

    def get_serializer_context(self):
        context = super().get_serializer_context()
        request: HttpRequest = context["request"]

        SchoolGroup = None

        try:
            if "group_id" in request.GET:
                context["group"] = SchoolGroup.objects.get(id=request.GET["group_id"])
            if "group_id" in request.data:
                context["group"] = SchoolGroup.objects.get(id=request.data["group_id"])
            if request.user:
                context["user"] = request.user
        except SchoolGroup.DoesNotExist:
            ...

        return context

    def list(self, request):
        pass

    def create(self, request):
        pass

    def retrieve(self, request, pk=None):
        pass

    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass
