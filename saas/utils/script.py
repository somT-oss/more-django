import random
import logging
import requests as r
import os
from dotenv import load_dotenv, find_dotenv
from faker import Faker
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
    - create users
    """
    def __init__(self) -> None:
        self.url = os.getenv("DEV_URL")
        self.port = os.getenv("DEV_SERVER_PORT")
        self.base_url = f"{self.url}:{self.port}/"
        self.password = "testing.321"
        self.fake = Faker()
        return None

    def create_users(self, count: int) -> int:
        """
        Create <count> number of users
        @param count: number of users to create
        """
        endpoint = "api/users/create-users"
        users_handler_url = self.base_url + endpoint
        logging.info(f"Base URL: {self.base_url}")
        logging.info(f"Endpoint called {endpoint}")
        logging.info(f"Full URL {users_handler_url}")
        print("")
        logging.info(f"Request to create {count} number of buyers initiated")
        try:
            is_seller_counter, is_buyer_counter = 0, 0  
            for _ in range(count):
                is_seller = random.choice([True, False])
                is_buyer = random.choice([True, False])

                print(is_seller, is_buyer)
                if is_buyer and is_seller:
                    is_seller = False
                
                payload = {
                    "first_name": self.fake.unique.first_name(),
                    "last_name": self.fake.unique.last_name(),
                    "email": self.fake.unique.email(),
                    "password": self.password,
                    "is_seller": is_seller,
                    "is_buyer": is_buyer,
                }
                if is_seller is True:
                     is_seller_counter += 1
                else:
                    is_buyer_counter += 1
                response = r.post(
                    url=users_handler_url,
                    data=payload
                )
                logging.info(f"JSON response: {response.json()}")
                logging.info(f"statusCode: {response.status_code}")
            logging.info(f"Done creating {count} number of users")
            logging.info(f"Created {is_seller_counter} number of seller(s)")
            logging.info(f"Created {is_buyer_counter} number of buyer(s)")
            return 0
        except Exception as e:
            logging.warning(f"{e}")

    def login_as_a_random_buyer(self, email, password) -> str:
        """
        Returns params {
            id: user_id,
            first_name: user first_name,
            last_name: user last_name,
            email: user email,
            tokens: {
                access: user access_token,
                refresh: user refresh_token
            }
        }
        """
        endpoint = "login-users/"
        login_url = self.base_url + endpoint
        payload = {
            "email": email,
            "password": password
        }
        try:
            response = r.post(
                url=login_url,
                data=payload
            )
            if response.status_code != 200:
                logging.warning("Unsuccessful login")
                return {
                    "error": "Unsuccessful login",
                    "statusCode": "response.status_code",
                    "response_json": f"{response.json()}"
                }
            return response.json()
        except Exception as e:
            logging.warning(f"{e} occurred")


def main():
    user_utils = UserFunctionalityHandler()

    sys_args: list = sys.argv[1:]

    if not sys_args:
        logging.info("Enter commands for loader...")
        print("")

    function_call_dict: dict = {}

    for command in sys_args:
        if ":" not in command:
            logging.warning(f"{command} is an invalid command")
            logging.info("Existing loader...")
            print("")
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
            logging.warning("Cannot create 0 users")
            return -1

    for key, value in function_call_dict.items():
        if key == 'create-user':
            user_utils.create_users(int(value))

if __name__ == "__main__":
    print("")
    logging.info("Script is up and grateful.. 🙏")
    main()
