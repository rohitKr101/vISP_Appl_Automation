import os
import time

from dotenv import load_dotenv
from p3270 import P3270Client

from TestCases.Login import Login

from TestCases.TC_02 import test_case_2
from TestCases.TC_03_05 import test_case_3_5
from TestCases.TC_04_06 import test_case_4_6
from TestCases.TC_07_08_10 import test_case_7_8_10
from TestCases.TC_09_11 import test_case_9_11
from TestCases.TC_12 import test_case_12
from TestCases.TC_13 import test_case_13
from TestCases.TC_14 import test_case_14
from TestCases.TC_15 import test_case_15
from TestCases.TC_16 import test_case_16
from TestCases.TC_17 import test_case_17

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
    # test_case_7_8_10(my_client, Username, Password)
    # test_case_9_11(my_client, Username, Password)
    # test_case_12(my_client, Username, Password)
    # test_case_13(my_client, Username, Password)
    # test_case_14(my_client, Username, Password)
    # test_case_15(my_client, Username, Password)
    # test_case_16(my_client, Username, Password)
    test_case_17(my_client, Username, Password)


if __name__ == "__main__":
    main()
