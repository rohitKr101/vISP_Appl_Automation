import os
import time

from dotenv import load_dotenv
from p3270 import P3270Client

from TestCases.TC_02 import test_case_2
from TestCases.TC_03_05 import test_case_3_5
from TestCases.TC_04_06 import test_case_4_6
from TestCases.TC_07_08_10 import test_case_7_8_10

load_dotenv(
    override=True
)  # load the .env file and override existing system environment variables if they exist

Hostname = os.getenv("HOSTNAME")
Username = os.getenv("USERNAME")
Password = os.getenv("PASSWORD")


def main():
    my_client = P3270Client(hostName=Hostname)

    # test_case_2(my_client, Username, Password)
    # test_case_3_5(my_client, Username, Password)
    # test_case_4_6(my_client, Username, Password)
    test_case_7_8_10(my_client, Username, Password)


if __name__ == "__main__":
    main()
