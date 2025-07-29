import logging
from app import constants as const
from django.conf import settings

class QrOperator:
    def __init__(self):
        self._logger = logging.getLogger(const.LOGGER_NAME)
        # self.service = ImportedProvider()

    def logger(self):
        """Return logger"""
        return self._logger

    def hello_world(self):
        some_venv = getattr(settings, 'SOME_VENV')
        return (
            'Hello world from "{{ cookiecutter.project_slug }}" BFF! '
            f'Some venv: "{some_venv}"'
        )