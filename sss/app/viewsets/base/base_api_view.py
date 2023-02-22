from rest_framework.views import APIView as _APIView

__all__ = ["APIView"]


class APIView(_APIView):
    def post(self, request):
        ...
