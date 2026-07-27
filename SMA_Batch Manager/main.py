import os
import time
from dotenv import load_dotenv
from p3270 import P3270Client



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

        

    else:
        print("Mainframe Connection Failed.")

    my_client.disconnect()
    print("Mainframe Disconnected.")


if __name__ == "__main__":
    main()
