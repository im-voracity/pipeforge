import os
import time

from dotenv import load_dotenv
from pipeforge.pipedrive import Pipedrive
from pipeforge.persons import Persons
from pipeforge.users import Users

load_dotenv()

company_domain = os.getenv("COMPANY_DOMAIN")
api_token = os.getenv("PERSONAL_API_TOKEN")

pipedrive = Pipedrive(company_domain=company_domain, api_token=api_token, log_level=10)
persons = Persons(pipedrive=pipedrive)
users = Users(pipedrive=pipedrive)
