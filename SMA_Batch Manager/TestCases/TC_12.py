from datetime import datetime
import time

from .utils import add_heading, fetch_ExpectedDate
from .Login import Login


def test_case_12(client, username, password):
    # SMABatchManager_Batch Creation_Create Batch with items from different departments

    if client.connect():
        print("Mainframe Connection Successful.")
        time.sleep(7)

        file_path = "Reports/TC_12_Report.html"
        add_heading(
            file_path,
            "TC_12_SMABatchManager_Batch Creation_Create Batch with items from different departments",
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
        client.sendText("item diff dept")
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

        

        # fetch_ExpectedDate(client, file_path)
        print("<-------------------Test Case 12 executed------------------->")


    else:
        print("Mainframe Connection Failed.")

    client.disconnect()
    print("Mainframe Disconnected.")