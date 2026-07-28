import os
import time

from dotenv import load_dotenv
from p3270 import P3270Client

from TestCases.TC_2 import test_case_2
from TestCases.TC_3 import test_case_3

load_dotenv(
    override=True
)  # load the .env file and override existing system environment variables if they exist

Hostname = os.getenv("HOSTNAME")
Username = os.getenv("USERNAME")
Password = os.getenv("PASSWORD")


def main():
    my_client = P3270Client(hostName=Hostname)

    # test_case_2(my_client, Username, Password)
    test_case_3(my_client, Username, Password)



if __name__ == "__main__":
    main()
