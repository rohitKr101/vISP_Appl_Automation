import time

from p3270.p3270 import P3270Client

from .utils import add_heading
from .Login import Login


def test_case_26(client: P3270Client, username, password):
    # SMABatchManager_Vendor Search_By Vendor name and Commodity
    if client.connect():
        print("Mainframe Connection Successful.")
        time.sleep(7)

        file_path = "Reports/TC_26_Report.html"
        add_heading(
            file_path,
            "TC026_SMABatchManager_Vendor Search_By Vendor name and Commodity",
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

        client.sendText("hallmark marketing comp")
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

        # Select Commodity
        client.sendPF(4)
        time.sleep(2)
        # client.saveScreen(file_path, dataType="txt")
        for _ in range(1):
            client.sendTab()
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

        print("<-------------------Test Case 26 executed------------------->")

    else:
        print("Mainframe Connection Failed.")

    client.disconnect()
    print("Mainframe Disconnected.")
