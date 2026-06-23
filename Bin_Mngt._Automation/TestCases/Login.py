import time


def login(my_client, username, password):
    if my_client.connect():
        print("Mainframe Connection Successful.")
        time.sleep(5)

        my_client.sendEnter()
        time.sleep(7)

        my_client.sendText(username)
        my_client.sendEnter()
        print("Username Entered")
        time.sleep(7)

        my_client.sendText(password)
        my_client.sendEnter()
        print("Password Entered")
        time.sleep(7)

        my_client.printScreen()