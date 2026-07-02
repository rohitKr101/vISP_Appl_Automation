import os
import time
from dotenv import load_dotenv
from p3270 import P3270Client

load_dotenv(
    override=True
)  # load the .env file and override existing system environment variables if they exist


def add_heading(file_name, heading):
    """Add an HTML heading to a file"""
    with open(file_name, "a") as f:
        f.write(
            f"<h2 style='background: rgb(0 0 0 / 88%);border-left: 20px solid #C62828;box-shadow: rgb(202, 201, 201) 0px 2px 10px 0px;color: #008000;font-size: 18px;font-weight: 600;line-height: 1.7em;padding: 10px;text-align: center;user-select: none;border-radius: 10px;'>{heading}</h2>\n"
        )


Hostname = os.getenv("HOSTNAME")
Username = os.getenv("USERNAME")
Password = os.getenv("PASSWORD")


def main():
    my_client = P3270Client(hostName=Hostname)
    save_name = "eWIC_Report.html"
    if my_client.connect():
        print("Mainframe Connection Successful.")
        time.sleep(7)

        # Login to the mainframe
        my_client.sendEnter()
        time.sleep(7)
        my_client.sendText(Username)
        my_client.sendEnter()
        print("Username Entered.")
        time.sleep(7)

        my_client.moveTo(15, 11)
        my_client.sendText(Password)
        my_client.sendEnter()
        print("Password Entered.")
        time.sleep(7)

        my_client.sendEnter()
        time.sleep(2)



    else:
        print("Mainframe Connection Failed.")

    my_client.disconnect()
    print("Mainframe Disconnected.")


if __name__ == "__main__":
    main()
