import logging, os

from django.conf import settings
from rest_framework import status

from app import constants
from app.restful import Restful

class BaseProvider:
    def __init__(self):
        self.logger = logging.getLogger(constants.LOGGER_NAME)
        self._service = Restful()
        self._authorization = None
        self.__headers = None
        self.mapfre_id = None

    @property
    def authorization(self):
        """Returns authorization for making the request."""
        return self._authorization

    @property
    def headers(self):
        """Returns headers to be used in every request"""
        if not self.__headers and self.authorization:
            self.__headers = {'Authorization': f'Bearer {self.authorization}'}
        return self.__headers
    
    def reset_headers(self):
        self.__headers = None

    def set_authorization(self, authorization):
        self._authorization = authorization
        self.reset_headers()

    def set_domain(self, venv_name):
        domain = getattr(settings, venv_name, None)
        self._service.set_domain(domain)


class QrProvider(BaseProvider):
    def __init__(self):
        super().__init__()
        self.set_domain('QR_APP_LOCATION') # base url from venv

    # @authorized_s2s
    def post_test(self, data):
        """
        Some example request to external service, using authorization
        """
        self.logger.debug('Calling to external service endpoint')
        endpoint = 'test'
        method_name = constants.HTTP_METHOD_POST
        response = self._service.make_request(
            endpoint=endpoint, method_name=method_name, headers=self.headers, params=data
        )
        self.logger.debug(f'Response status code: {response.status_code}')
        self.logger.debug(f'Response json: {response.json()}')
        return response.status_code, response.json()
