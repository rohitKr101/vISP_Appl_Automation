import os
import time
from dotenv import load_dotenv
from p3270 import P3270Client
from utils import add_heading

from TC_01 import testCase_1
from TC_02 import testCase_2
from Login import login

load_dotenv(
    override=True
)  # load the .env file and override existing system environment variables if they exist

Hostname = os.getenv("HOSTNAME")
Username = os.getenv("USERNAME")
Password = os.getenv("PASSWORD")


def main():
    my_client = P3270Client(hostName=Hostname)
    save_path = "PV_Report.html"
    if my_client.connect():
        print("Mainframe Connection Successful.")
        time.sleep(7)
        add_heading(save_path, "pSMA Price Verification Test Cases")

        login(my_client, Username, Password)
        testCase_1(my_client, save_path)
        testCase_2(my_client, save_path)

    else:
        print("Mainframe Connection Failed.")

    my_client.disconnect()
    print("Mainframe disconnected.")


if __name__ == "__main__":
    main()
