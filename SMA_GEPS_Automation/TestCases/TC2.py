import time
from TestCases.Login import Login
from .utils import add_heading


def test_case_2(my_client, username, password):
    """Test Case 2: Check UPC's"""
    save_path = "Reports/SMA_GEPS_TC2.html"
    add_heading(save_path, "SMA Great Entertaining Price Support")
    add_heading(save_path, "TC2: Check upc in geupcs.txt file")
    login = Login(my_client, username, password)
    login.login()

    add_heading(save_path, "1. Login to lab box 6949 and enter SUDO command.")
    my_client.saveScreen(save_path, dataType="txt")

    my_client.sendText("sudo /bin/su - sma_user")
    my_client.sendEnter()
    time.sleep(5)
    my_client.saveScreen(save_path, dataType="txt")

    my_client.sendText("cd /opt/sma/transfer_files")
    my_client.sendEnter()
    time.sleep(2)
    my_client.sendText("ls -lrt")
    my_client.sendEnter()
    time.sleep(2)
    add_heading(save_path,"2. Go to /opt/sma/transfer_files and check if geupcs.txt is present.",)
    my_client.saveScreen(save_path, dataType="txt")

    my_client.sendText("cat geupcs.txt")
    time.sleep(2)
    add_heading(save_path, "3. Display geupcs.txt and check if the UPC’s are present.")
    my_client.saveScreen(save_path, dataType="txt")

    my_client.sendEnter()
    time.sleep(6)
    my_client.saveScreen(save_path, dataType="txt")

    print("<---------------TC 02 - Executed-------------->")
