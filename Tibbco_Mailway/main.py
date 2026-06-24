import os
import time
from dotenv import load_dotenv
from p3270 import P3270Client

from TestCases.TC1 import test_case_1
from TestCases.TC2 import test_case_2

load_dotenv(
    override=True
)  # load the .env file and override existing system environment variables if they exist

Hostname = os.getenv("HOSTNAME")
Username = os.getenv("USERNAME")
Password = os.getenv("PASSWORD")


def main():
    my_client = P3270Client(hostName=Hostname)

    if my_client.connect():
        print("Mainframe Connection Successful.")
        time.sleep(7)

        test_case_1(my_client, Username, Password)
        test_case_2(my_client, Username, Password)

    else:
        print("Mainframe Connection Failed.")

    my_client.disconnect()
    print("Mainframe Disconnected.")


if __name__ == "__main__":
    main()
