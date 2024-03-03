import requests.exceptions
import urllib.parse
import coloredlogs
import requests
import logging
import sys

from typing import List, Dict, Any, Optional

# Base Logging Configs
logger = logging.getLogger(__name__)

# Coloredlogs Configs
coloredFormatter = coloredlogs.ColoredFormatter(
    fmt='[%(name)s] %(asctime)s  %(message)s',
    level_styles=dict(
        debug=dict(color='white'),
        info=dict(color='blue'),
        warning=dict(color='yellow', bright=True),
        error=dict(color='red', bold=True, bright=True),
        critical=dict(color='black', bold=True, background='red'),
    ),
    field_styles=dict(
        name=dict(color='white'),
        asctime=dict(color='white'),
        funcName=dict(color='white'),
        lineno=dict(color='white'),
    )
)

# Console Handler Configs
ch = logging.StreamHandler(stream=sys.stdout)
ch.setFormatter(fmt=coloredFormatter)
logger.addHandler(hdlr=ch)
logger.setLevel(level=logging.CRITICAL)


class Pipedrive:
    # URL Configs
    BASE_URL = "https://{COMPANYDOMAIN}.pipedrive.com/api/v1"

    def __init__(self, company_domain: str, api_token: str, log_level: int = logging.CRITICAL) -> None:
        """
        Initializes the Pipedrive API Client. Full docs can be found at https://developers.pipedrive.com/docs/api/v1
        :param company_domain: The subdomain dedicated to a company in Pipedrive
        :param api_token: The Personal API Token generated in Pipedrive
        """
        self.company_domain = company_domain
        self.api_token = api_token
        self.base_url = self.BASE_URL.format(COMPANYDOMAIN=company_domain)

        self.logger = logger  # Use the logger set up at the module level
        self.logger.setLevel(log_level)
        self.logger.info("Coloredlogs is available.")

    @staticmethod
    def url_encode(input_string: str) -> str:
        return urllib.parse.quote_plus(input_string)

    @staticmethod
    def build_payload(**kwargs: Any) -> Dict[str, Any]:
        """
        Builds a parameters dictionary with the given kwargs, ignoring the ones with None value.
        :param kwargs: Expected kwargs can be found in the ""
        :return: Dict[str, Any]: The built params as dictionary
        """
        params = {}
        for key, value in kwargs.items():
            if value is not None:
                params[key.lower()] = str(value)
        return params

    def make_request(self, method: Any, url: str, params: Dict = None, payload: Dict = None, files: Dict = None, log_level: int = None):
        """
        Makes a request to the given url.
        :param method: The request method (e.g, requests.get, requests.post).
        :param url: The URL to make the request to.
        :param params: The parameters to be sent with the request.
        :param payload: The payload to be sent with the request.
        :param files: The files to be sent with the request.
        :param log_level: The logging level for this method (default is None, inherits from class level).
        :return: The JSON response if the request is successful, error is returned otherwise.
        """

        if log_level is not None:
            logger = logging.getLogger(__name__)
            logger.setLevel(log_level)
        try:
            # self.logger.debug(f"Request URL: {self.base_url}")
            self.logger.debug(f"API Token: {self.api_token}")

            if params is None:
                params = {}
            request_params = {**params, 'api_token': self.api_token}

            if payload is None:
                payload = {}

            if files is None:
                files = {}

            response = method(url=f"{url}", params=request_params, json=payload, files=files)
            self.logger.debug(response.url)
            if response.text:
                self.logger.debug(f"Response content: {response.json()}")
            response.raise_for_status()
            return response.json()

        except requests.exceptions.HTTPError as e:
            self.logger.error(f"HTTP Error {e.response.status_code}: {e.response.text}")
            raise e
        except requests.exceptions.RequestException as e:
            self.logger.error(f"Error making request to {url}: {e}")
            raise e

