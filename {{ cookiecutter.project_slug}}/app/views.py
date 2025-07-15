from django.http import JsonResponse
from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema
import logging
from app import constants as const, operations

class BaseViewSet(viewsets.ViewSet):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._logger = logging.getLogger(const.LOGGER_NAME)

    @property
    def logger(self):
        """Return logger"""
        return self._logger


class TestViewSet(BaseViewSet):

    authentication_classes = []
    permission_classes = [AllowAny]


    @extend_schema(
        tags=['Test'],
        summary="""Hello world""",
        description="""
            Example for hello world
        """,
    )
    def hello_world(self, request):
        """"""
        res = operations.QrOperator().hello_world()
        self.logger.debug('Received request')
        return Response(data=res, status=status.HTTP_200_OK)



