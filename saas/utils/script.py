import random
import logging
import requests as r
import os
from dotenv import load_dotenv, find_dotenv
from faker import Faker
from typing import Callable
import sys 

load_dotenv(find_dotenv())


logging.basicConfig(
    level=logging.INFO,
    format="{asctime} - {levelname} - {message}",
    style="{",
    datefmt="%Y-%m-%d: %H:%M",
    handlers=[
        logging.StreamHandler()
    ]
)


class UserFunctionalityHandler:
    """
    Handles functionality for users such as:
    - create buyers
    - create sellers
    """
    def __init__(self) -> None:
        self.url = os.getenv("DEV_URL")
        self.port = os.getenv("DEV_SERVER_PORT")
        self.base_url = f"{self.url}:{self.port}/"
        self.password = "testing.321"
        self.hostels = ['jaja', 'biobaku', 'eni_njoku', 'mariere']
        self.room_names = ["110", "112", "113", "114", "115"]
        self.fake = Faker()
        return None

    def create_buyers(self, count: int) -> int:
        """
        Create <count> number of buyers
        @param count: number of sellers to create
        """
        endpoint = "users/create-buyers/"
        users_handler_url = self.base_url + endpoint
        logging.info(f"Base URL: {self.base_url}")
        logging.info(f"Endpoint called {endpoint}")
        logging.info(f"Full URL {users_handler_url}")
        print("")
        logging.info(f"Request to create {count} number of buyers initiated")
        try:

            for _ in range(count):
                payload = {
                    "first_name": self.fake.unique.first_name(),
                    "last_name": self.fake.unique.last_name(),
                    "email": self.fake.unique.email(),
                    "password": self.password,
                    "hostel": random.choice(self.hostels),
                    "room_name": random.choice(self.room_names),
                    "is_seller": random.choice([True, False])
                }
                response = r.post(
                    url=users_handler_url,
                    data=payload
                )
                logging.info(f"statusCode: {response.status_code}")
            logging.info(f"Done creating {count} number of buyers")
            return 0
        except Exception as e:
            logging.warning(f"{e}")

    @staticmethod
    def create_sellers(count: int) -> int:
        """
        Create <count> number of sellers
        @param count: number of sellers to create
        """
        return 0


def main():
    user_utils = UserFunctionalityHandler()

    sys_args: list = sys.argv[1:]

    if not sys_args:
        logging.info("Enter commands for loader...")
    
    function_call_dict: dict = {}

    for command in sys_args:
        if ":" not in command:
            logging.warning(f"{command} is an invalid command")
            logging.info(f"Existing loader...")
            return -1
        args = command.split(":")
        function_call = args[0]
        count = args[1]
        function_call_dict[function_call] = count

    for key, value in function_call_dict.items():
        if not value.isdigit():
            logging.warning(f"Invalid value: {value} for {key}")
            return -1 

        if value == "0":
            logging.warning(f"Cannot create 0 users")
            return -1 

    for key, value in function_call_dict.items():
        if key == 'create-buyer':
            user_utils.create_buyers(int(value))
        elif key == 'create-seller':
            user_utils.create_sellers(int(value))

        
if __name__ == "__main__":
    print("")
    print("")
    logging.info("Script is up and grateful.. 🙏")
    main()
