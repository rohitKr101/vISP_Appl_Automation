from datetime import datetime
import time

from .utils import add_heading
from .Login import Login


def test_case_13(client, username, password):
    # SMABatchManager_View or Edit Item
    if client.connect():
        print("Mainframe Connection Successful.")
        time.sleep(7)

        file_path = "Reports/TC_13_Report.html"
        add_heading(
            file_path,
            "TC_13_SMABatchManager_View or Edit Item",
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
        client.sendText("item description edit")
        time.sleep(2)
        client.saveScreen(file_path, dataType="txt")

        # Add items from different departments
        client.sendPF(12)
        time.sleep(2)

        client.sendTab()
        time.sleep(2)
        client.sendText("41110")
        time.sleep(2)
        client.sendEnter()
        time.sleep(2)
        client.saveScreen(file_path, dataType="txt")

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

        # Edit Item Description
        client.sendPF(7)
        time.sleep(2)
        client.sendText("Updated Item Description")
        time.sleep(2)
        client.saveScreen(file_path, dataType="txt")
        client.sendPF(12)
        time.sleep(2)
        client.saveScreen(file_path, dataType="txt")

        # Add Pricing Information
        client.sendPF(7)
        time.sleep(2)
        for _ in range(7):
            client.sendTab()
            time.sleep(1)

        client.sendText("2")  # EDLP Unit
        client.sendTab()
        time.sleep(1)

        client.sendText("1")  # EDLP Price
        client.sendTab()
        time.sleep(1)

        client.sendText("1")  # Promo Unit
        client.sendTab()
        time.sleep(1)

        client.sendText("0")  # Promo Price
        client.sendTab()
        client.sendTab()
        time.sleep(1)

        client.sendText("3")  # Promo Type
        client.sendTab()
        time.sleep(5)

        client.saveScreen(file_path, dataType="txt")

        client.sendPF(12)
        time.sleep(2)
        client.saveScreen(file_path, dataType="txt")

        print("<-------------------Test Case 13 executed------------------->")

    else:
        print("Mainframe Connection Failed.")

    client.disconnect()
    print("Mainframe Disconnected.")
