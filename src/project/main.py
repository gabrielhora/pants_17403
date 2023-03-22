from datetime import datetime

import boto3
from lib.my_lib.my_lib import say_hello


def main():
    boto3.setup_default_session(region_name="localhost")
    print(f"Today is: {datetime.today()}")
    print(say_hello("John Doe"))
