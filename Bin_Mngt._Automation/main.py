import os
from dotenv import load_dotenv
from p3270 import P3270Client

from TestCases.Login import login
from TestCases.testCase1 import test_case_1

load_dotenv(override=True) # load the .env file and override existing system environment variables if they exist

Hostname = os.getenv("HOSTNAME")
Username = os.getenv("USERNAME")
Password = os.getenv("PASSWORD")


def main():
    my_client = P3270Client(hostName=Hostname)

    login(my_client, Username, Password)
    # test_case_1(my_client, Username, Password)

if __name__ == "__main__":
    main()