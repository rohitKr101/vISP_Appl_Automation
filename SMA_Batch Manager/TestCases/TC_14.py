from datetime import datetime
from http import client
import time

from .utils import add_heading
from .Login import Login


def test_case_14(client, username, password):
    # SMABatchManager_View or Edit Item_Edit_UOM
    if client.connect():
        print("Mainframe Connection Successful.")
        time.sleep(7)

        file_path = "Reports/TC_14_Report.html"
        add_heading(
            file_path,
            "TC_14_SMABatchManager_View or Edit Item_Edit_UOM",
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
        client.sendText("Edit UOM")
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

        client.sendTab()
        time.sleep(2)
        client.sendKeys("t")
        time.sleep(2)
        client.saveScreen(file_path, dataType="txt")

        # List all tags
        client.sendPF(5)
        time.sleep(2)

        # No. of tabs to choose the required tag
        for _ in range(2):
            client.sendTab()
            time.sleep(2)
        client.saveScreen(file_path, dataType="txt")

        client.sendPF(12)
        time.sleep(2)
        client.saveScreen(file_path, dataType="txt")
        client.sendPF(12)
        time.sleep(2)
        client.saveScreen(file_path, dataType="txt")

        # View or Edit Item
        client.sendPF(7)
        time.sleep(2)
        client.saveScreen(file_path, dataType="txt")

        client.sendPF(4)  # Edit UOM
        time.sleep(2)
        client.saveScreen(file_path, dataType="txt")

        client.sendPF(2)  # List UOM
        time.sleep(2)
        client.saveScreen(file_path, dataType="txt")

        client.sendPF(12)
        time.sleep(2)
        client.saveScreen(file_path, dataType="txt")

        print("<-------------------Test Case 14 executed------------------->")

    else:
        print("Mainframe Connection Failed.")

    client.disconnect()
    print("Mainframe Disconnected.")
