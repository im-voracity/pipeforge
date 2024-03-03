from typing import List, Dict, Any
from .pipedrive import Pipedrive
import requests

class Persons:
    """
    The Persons class provides methods to interact with the 'persons' endpoint of the Pipedrive API.
    """

    def __init__(self, pipedrive: Pipedrive):
        """
        Initialize a new instance of the Persons class.

        :param pipedrive: An instance of the Pipedrive class.
        """
        self.pipedrive = pipedrive

    def get_all(self) -> List[Dict[str, Any]]:
        """
        Get all persons in the company.

        :return: A list of dictionaries, each representing a person.
        """
        method_url = f"{self.pipedrive.base_url}/persons"
        return self.pipedrive.make_request(method=requests.get, url=method_url)

    def search(self, term: str, **kwargs: Any) -> List[Dict[str, Any]]:
        """
        Search all persons by name, email, phone, notes and/or custom fields.

        :param term: A string to search for.
        :param kwargs: Any additional query/filtering parameters supported.
        :return: A list of dictionaries, each representing a match result.
        """
        method_url = f"{self.pipedrive.base_url}/persons/search"
        params = self.pipedrive.build_payload(term=self.pipedrive.url_encode(term.lower()), **kwargs)
        return self.pipedrive.make_request(method=requests.get, url=method_url, params=params)

    def get_details(self, person_id: int, **kwargs: Any) -> Dict[str, Any]:
        """
        Get details of a person by ID.

        :param person_id: The ID of the person.
        :param kwargs: Any additional query/filtering parameters supported.
        :return: A dictionary representing the person details.
        """
        method_url = f"{self.pipedrive.base_url}/persons/{person_id}"
        params = self.pipedrive.build_payload(person_id=person_id, **kwargs)
        return self.pipedrive.make_request(method=requests.get, url=method_url, params=params)

    def list_activities_associated(self, person_id: int, **kwargs: Any) -> List[Dict[str, Any]]:
        """
        List all activities associated with a person.

        :param person_id: The ID of the person.
        :param kwargs: Any additional query/filtering parameters supported.
        :return: A list of dictionaries, each representing an activity.
        """
        method_url = f"{self.pipedrive.base_url}/persons/{person_id}/activities"
        params = self.pipedrive.build_payload(**kwargs)
        return self.pipedrive.make_request(method=requests.get, url=method_url, params=params)

    def list_deals_associated(self, person_id: int, **kwargs: Any) -> List[Dict[str, Any]]:
        """
        List all deals associated with a person.

        :param person_id: The ID of the person.
        :param kwargs: Any additional query/filtering parameters supported.
        :return: A list of dictionaries, each representing a deal.
        """
        method_url = f"{self.pipedrive.base_url}/persons/{person_id}/deals"
        params = self.pipedrive.build_payload(**kwargs)
        return self.pipedrive.make_request(method=requests.get, url=method_url, params=params)

    def list_files_attached(self, person_id: int, **kwargs: Any) -> List[Dict[str, Any]]:
        """
        List all files attached to a person.

        :param person_id: The ID of the person.
        :param kwargs: Any additional query/filtering parameters supported.
        :return: A list of dictionaries, each representing a file.
        """
        method_url = f"{self.pipedrive.base_url}/persons/{person_id}/files"
        params = self.pipedrive.build_payload(**kwargs)
        return self.pipedrive.make_request(method=requests.get, url=method_url, params=params)

    def list_updates(self, person_id: int, **kwargs: Any) -> List[Dict[str, Any]]:
        """
        List all updates associated with a person.

        :param person_id: The ID of the person.
        :param kwargs: Any additional query/filtering parameters supported.
        :return: A list of dictionaries, each representing an update.
        """
        method_url = f"{self.pipedrive.base_url}/persons/{person_id}/flow"
        params = self.pipedrive.build_payload(**kwargs)
        return self.pipedrive.make_request(method=requests.get, url=method_url, params=params)

    def list_followers(self, person_id: int, **kwargs: Any) -> List[Dict[str, Any]]:
        """
        List all followers of a person.

        :param person_id: The ID of the person.
        :param kwargs: Any additional query/filtering parameters supported.
        :return: A list of dictionaries, each representing a follower.
        """
        method_url = f"{self.pipedrive.base_url}/persons/{person_id}/followers"
        params = self.pipedrive.build_payload(**kwargs)
        return self.pipedrive.make_request(method=requests.get, url=method_url, params=params)

    def list_mail_messages(self, person_id: int, **kwargs: Any) -> List[Dict[str, Any]]:
        """
        List all mail messages associated with a person.

        :param person_id: The ID of the person.
        :param kwargs: Any additional query/filtering parameters supported.
        :return: A list of dictionaries, each representing a mail message.
        """
        method_url = f"{self.pipedrive.base_url}/persons/{person_id}/mailMessages"
        params = self.pipedrive.build_payload(**kwargs)
        return self.pipedrive.make_request(method=requests.get, url=method_url, params=params)

    def list_permitted_users(self, person_id: int, **kwargs: Any) -> List[Dict[str, Any]]:
        """
        List all permitted users of a person.

        :param person_id: The ID of the person.
        :param kwargs: Any additional query/filtering parameters supported.
        :return: A list of dictionaries, each representing a permitted user.
        """
        method_url = f"{self.pipedrive.base_url}/persons/{person_id}/permittedUsers"
        params = self.pipedrive.build_payload(**kwargs)
        return self.pipedrive.make_request(method=requests.get, url=method_url, params=params)

    def list_products_associated(self, person_id: int, **kwargs: Any) -> List[Dict[str, Any]]:
        """
        List all products associated with a person.

        :param person_id: The ID of the person.
        :param kwargs: Any additional query/filtering parameters supported.
        :return: A list of dictionaries, each representing a product.
        """
        method_url = f"{self.pipedrive.base_url}/persons/{person_id}/products"
        params = self.pipedrive.build_payload(**kwargs)
        return self.pipedrive.make_request(method=requests.get, url=method_url, params=params)

    def add(self, name: str, **kwargs: Any) -> Dict[str, Any]:
        """
        Add a new person.

        :param name: The name of the person.
        :param kwargs: Any additional query/filtering parameters supported.
        :return: A dictionary representing the added person.
        """
        method_url = f"{self.pipedrive.base_url}/persons"
        payload = self.pipedrive.build_payload(name=name, **kwargs)
        return self.pipedrive.make_request(method=requests.post, url=method_url, payload=payload)

    def add_follower(self, person_id: int, user_id: int) -> Dict[str, Any]:
        """
        Add a follower to a person.

        :param person_id: The ID of the person.
        :param user_id: The ID of the user to be added as a follower.
        :return: A dictionary representing the added follower.
        """
        method_url = f"{self.pipedrive.base_url}/persons/{person_id}/followers"
        params = self.pipedrive.build_payload(person_id=person_id)
        payload = self.pipedrive.build_payload(user_id=user_id)
        return self.pipedrive.make_request(method=requests.post, url=method_url, payload=payload, params=params)

    def add_picture(self, person_id: int, image: str) -> Dict[str, Any]:
        """
        Add a picture to a person.

        :param person_id: The ID of the person.
        :param image: The path to the image file.
        :return: A dictionary representing the added picture.
        """
        self.pipedrive.logger.critical("This method is not working as expected. It's returning a 500 (Internal server "
                                       "error).")
        method_url = f"{self.pipedrive.base_url}/persons/{person_id}/picture"
        files = {'file': open(image, 'rb')}
        return self.pipedrive.make_request(method=requests.post, url=method_url, files=files)

    def update(self, person_id: int, **kwargs: Any) -> Dict[str, Any]:
        """
        Update a person.

        :param person_id: The ID of the person.
        :param kwargs: Any additional query/filtering parameters supported.
        :return: A dictionary representing the updated person.
        """
        method_url = f"{self.pipedrive.base_url}/persons/{person_id}"
        payload = self.pipedrive.build_payload(**kwargs)
        return self.pipedrive.make_request(method=requests.put, url=method_url, payload=payload)

    def merge(self, person_id: int, merge_with_id: int) -> Dict[str, Any]:
        """
        Merge a person with another.

        :param person_id: The ID of the person.
        :param merge_with_id: The ID of the person to merge with.
        :return: A dictionary representing the merged person.
        """
        method_url = f"{self.pipedrive.base_url}/persons/{person_id}/merge"
        params = self.pipedrive.build_payload(person_id=person_id)
        payload = self.pipedrive.build_payload(merge_with_id=merge_with_id)
        return self.pipedrive.make_request(method=requests.put, url=method_url, payload=payload, params=params)

    def bulk_delete(self, person_ids: List[int]) -> Dict[str, Any]:
        """
        Bulk delete persons.

        :param person_ids: A list of IDs of the persons to be deleted.
        :return: A dictionary representing the deleted persons.
        """
        request_ids = ','.join(map(str, person_ids))
        method_url = f"{self.pipedrive.base_url}/persons"
        payload = self.pipedrive.build_payload(ids=request_ids)
        return self.pipedrive.make_request(method=requests.delete, url=method_url, payload=payload)

    def delete(self, person_id: int) -> Dict[str, Any]:
        """
        Delete a person.

        :param person_id: The ID of the person.
        :return: A dictionary representing the deleted person.
        """
        method_url = f"{self.pipedrive.base_url}/persons/{person_id}"
        return self.pipedrive.make_request(method=requests.delete, url=method_url)

    def delete_follower(self, person_id: int, follower_id: int) -> Dict[str, Any]:
        """
        Delete a follower from a person.

        :param person_id: The ID of the person.
        :param follower_id: The ID of the follower.
        :return: A dictionary representing the deleted follower.
        """
        method_url = f"{self.pipedrive.base_url}/persons/{person_id}/followers/{follower_id}"
        return self.pipedrive.make_request(method=requests.delete, url=method_url)

    def delete_picture(self, person_id: int) -> Dict[str, Any]:
        """
        Delete a picture from a person.

        :param person_id: The ID of the person.
        :return: A dictionary representing the deleted picture.
        """
        method_url = f"{self.pipedrive.base_url}/persons/{person_id}/picture"
        return self.pipedrive.make_request(method=requests.delete, url=method_url)
