import requests
import logging
from urllib.parse import urljoin

class Restful:
    def __init__(self):
        self.logger = logging.getLogger("RestfulClient")
        self.base_url = None  # Default: no domain

    def set_domain(self, domain_key):
        """
        Sets the base domain for future requests, using an environment variable key.
        """
        self.base_url = domain_key
        self.logger.error(f"Domain set to: {self.base_url}")

    def make_request(self, endpoint, method_name='GET', headers=None, params=None):
        method_name = method_name.upper()
        url = self.base_url + f"/{endpoint}"

        self.logger.debug(f"[HTTP {method_name}] Request to {url}")
        self.logger.debug(f"Headers: {headers}")
        self.logger.debug(f"Payload: {params}")

        try:
            if method_name == 'GET':
                response = requests.get(url, headers=headers, params=params)
            elif method_name == 'POST':
                response = requests.post(url, headers=headers, json=params)
            elif method_name == 'PUT':
                response = requests.put(url, headers=headers, json=params)
            elif method_name == 'DELETE':
                response = requests.delete(url, headers=headers, json=params)
            else:
                raise ValueError(f"Unsupported HTTP method: {method_name}")

            self.logger.debug(f"[HTTP {method_name}] Response status: {response.status_code}")
            try:
                self.logger.debug(f"Response JSON: {response.json()}")
            except ValueError:
                self.logger.debug(f"Response Text: {response.text}")

            return response

        except requests.RequestException as e:
            self.logger.error(f"HTTP request to {url} failed: {e}")
            self.logger.error(f"HTTP request to {url} failed: {e}")
            raise RuntimeError(f"HTTP request failed: {e}") from e