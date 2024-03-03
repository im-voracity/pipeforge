import os
import unittest
from unittest.mock import Mock
from pipeforge.pipedrive import Pipedrive
from pipeforge.persons import Persons
from dotenv import load_dotenv

load_dotenv()

company_domain = os.getenv("COMPANY_DOMAIN")
api_token = os.getenv("PERSONAL_API_TOKEN")


class TestPersons(unittest.TestCase):
    def setUp(self):
        self.pipedrive = Pipedrive(company_domain=company_domain, api_token=api_token)
        self.persons = Persons(self.pipedrive)
        self.pipedrive.make_request = Mock()

    def test_persons_get_all_returns_all_persons(self):
        self.pipedrive.make_request.return_value = [{'id': 1, 'name': 'John Doe'}, {'id': 2, 'name': 'Jane Doe'}]
        result = self.persons.get_all()
        self.assertEqual(len(result), 2)

    def test_search_returns_matching_persons(self):
        self.pipedrive.make_request.return_value = [{'id': 1, 'name': 'John Doe'}]
        result = self.persons.search('John')
        self.assertEqual(len(result), 1)

    def test_get_details_returns_correct_person(self):
        self.pipedrive.make_request.return_value = {'id': 1, 'name': 'John Doe'}
        result = self.persons.get_details(1)
        self.assertEqual(result['name'], 'John Doe')

    def test_add_creates_new_person(self):
        self.pipedrive.make_request.return_value = {'id': 1, 'name': 'John Doe'}
        result = self.persons.add('John Doe')
        self.assertEqual(result['name'], 'John Doe')

    def test_update_modifies_existing_person(self):
        self.pipedrive.make_request.return_value = {'id': 1, 'name': 'Jane Doe'}
        result = self.persons.update(1, name='Jane Doe')
        self.assertEqual(result['name'], 'Jane Doe')

    def test_delete_removes_existing_person(self):
        self.pipedrive.make_request.return_value = {'success': True}
        result = self.persons.delete(1)
        self.assertTrue(result['success'])


if __name__ == '__main__':
    unittest.main()
