import time

from .utils import add_heading


class Login:

    def __init__(self, my_client, Username, Password):
        self.my_client = my_client
        self.Username = Username
        self.Password = Password

    def login(self):
        self.my_client.sendEnter()
        time.sleep(5)

        self.my_client.sendText(self.Username)
        self.my_client.sendEnter()
        print("Username Entered")
        time.sleep(5)

        self.my_client.sendText(self.Password)
        self.my_client.sendEnter()
        print("Password Entered")
        time.sleep(5)

        self.my_client.sendText("export TERM=xterm")
        self.my_client.sendEnter()
        time.sleep(2)
