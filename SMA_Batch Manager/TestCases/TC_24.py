import time

from p3270.p3270 import P3270Client

from .utils import add_heading
from .Login import Login


def test_case_24(client: P3270Client, username, password):
    # SMABatchManager_Vendor Search_By Vendor name
    if client.connect():
        print("Mainframe Connection Successful.")
        time.sleep(7)

        file_path = "Reports/TC_24_Report.html"
        add_heading(
            file_path,
            "TC_24_SMABatchManager_Vendor Search_By Vendor name",
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
        client.sendText("vendor search")
        time.sleep(2)
        client.sendPF(12)
        time.sleep(2)

        client.saveScreen(file_path, dataType="txt")

        # Vendor Search
        client.sendPF(5)
        time.sleep(2)
        client.saveScreen(file_path, dataType="txt")

        # Vendor Name
        client.sendTab()
        time.sleep(2)

        client.sendText("hallmark marketing")
        time.sleep(2)
        client.saveScreen(file_path, dataType="txt")

        # Vendor Number List
        client.sendPF(4)
        time.sleep(2)
        client.saveScreen(file_path, dataType="txt")

        # Process
        client.sendPF(12)
        time.sleep(2)
        client.saveScreen(file_path, dataType="txt")

        # Accept
        client.sendPF(12)
        time.sleep(5)
        client.saveScreen(file_path, dataType="txt")

        print("<-------------------Test Case 24 executed------------------->")

    else:
        print("Mainframe Connection Failed.")

    client.disconnect()
    print("Mainframe Disconnected.")
