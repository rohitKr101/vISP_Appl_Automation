from datetime import datetime
import time

from .utils import add_heading
from .Login import Login


def test_case_16(client, username, password):
    # SMABatchManager_View Item information
    if client.connect():
        print("Mainframe Connection Successful.")
        time.sleep(7)

        file_path = "Reports/TC_16_Report.html"
        add_heading(
            file_path,
            "TC_16_SMABatchManager_View Item information",
        )
        LOGIN = Login(client, username, password)
        LOGIN.login()

        client.sendText("sudo /bin/su - g06949cp1")
        client.sendEnter()
        time.sleep(2)

        # Select Shelf Management Systems
        client.sendKeys("s")
        time.sleep(2)
        client.sendEnter()
        time.sleep(2)

        # Select Store Batch Manager
        client.sendEnter()
        time.sleep(2)

        # Select Batch Create
        client.sendKeys("b")
        time.sleep(2)
        client.saveScreen(file_path, dataType="txt")
        client.sendEnter()
        time.sleep(2)
        client.sendText("Item Info")
        time.sleep(2)
        client.saveScreen(file_path, dataType="txt")

        # Add UPC
        client.sendPF(12)
        time.sleep(2)
        client.sendText("4011")
        time.sleep(2)
        client.sendEnter()
        time.sleep(2)
        client.saveScreen(file_path, dataType="txt")

        # Open Item Info
        client.sendPF(9)
        time.sleep(2)
        client.saveScreen(file_path, dataType="txt")

        print("<-------------------Test Case 16 executed------------------->")

    else:
        print("Mainframe Connection Failed.")

    client.disconnect()
    print("Mainframe Disconnected.")
