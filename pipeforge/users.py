from typing import List, Dict, Any
from .pipedrive import Pipedrive
import requests


class Users:
    def __init__(self, pipedrive: Pipedrive):
        self.pipedrive = pipedrive

    def get_all(self) -> List[Dict[str, Any]]:
        """
        Get all users in the company
        :return: List of users
        """
        method_url = f"{self.pipedrive.base_url}/users"
        return self.pipedrive.make_request(method=requests.get, url=method_url)
