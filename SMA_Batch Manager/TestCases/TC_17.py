from datetime import datetime
import time


from .utils import add_heading
from .Login import Login


def test_case_17(client, username, password):
    # SMABatchManager_Update quantity_For a batch with single batch line
    if client.connect():
        print("Mainframe Connection Successful.")
        time.sleep(7)

        file_path = "Reports/TC_17_Report.html"
        add_heading(
            file_path,
            "TC_17_SMABatchManager_Update quantity_For a batch with single batch line",
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

        # Select Tag
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

        # Update Quantity
        client.sendPF(8)
        time.sleep(2)
        client.saveScreen(file_path, dataType="txt")

        client.sendText(3)
        time.sleep(2)
        client.saveScreen(file_path, dataType="txt")

        client.sendPF(12)
        time.sleep(2)
        client.saveScreen(file_path, dataType="txt")

        print("<-------------------Test Case 17 executed------------------->")

    else:
        print("Mainframe Connection Failed.")

    client.disconnect()
    print("Mainframe Disconnected.")
