import time


def login(my_client, Username, Password):

    my_client.sendEnter()
    time.sleep(5)
    my_client.sendText(Username)
    my_client.sendEnter()
    print("Username Entered")
    time.sleep(5)

    my_client.sendText(Password)
    my_client.sendEnter()
    print("Password Entered")
    time.sleep(5)

    my_client.sendText("export TERM=xterm")
    my_client.sendEnter()
    time.sleep(2)

    my_client.sendText("sudo /bin/su - sma_user")
    my_client.sendEnter()
    time.sleep(5)