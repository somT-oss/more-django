import random
import logging
import requests as r
import os
from dotenv import load_dotenv, find_dotenv
from faker import Faker


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
        self.base_url = f"{self.url}:{self.port}"
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
        users_handler_url = self.base_url + '/users/handler/'
        logging.info(f"Base URL: {self.base_url}")
        logging.info(f"Request to create {count} number of buyers initiated")

        try:
            for _ in range(count+1):
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
    print(user_utils.create_buyers(2))


if __name__ == "__main__":
    logging.info("Script is up and grateful.. 🙏")
    main()
