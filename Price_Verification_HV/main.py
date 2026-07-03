import os
import time
from dotenv import load_dotenv
from p3270 import P3270Client

from Test_Case import testCase1
from Login import login


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

        # login(my_client, Username, Password)
        testCase1(my_client, Username, Password)

    else:
        print("Mainframe Connection Failed.")

    my_client.disconnect()
    print("Mainframe disconnected.")


if __name__ == "__main__":
    main()
