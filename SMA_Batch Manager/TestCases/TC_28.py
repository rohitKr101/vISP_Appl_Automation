import time

from p3270.p3270 import P3270Client

from .utils import add_heading
from .Login import Login


def test_case_28(client: P3270Client, username, password):
    # SMABatchManager_Compressed UPC with Sign
    if client.connect():
        print("Mainframe Connection Successful.")
        time.sleep(7)

        file_path = "Reports/TC_28_Report.html"
        add_heading(
            file_path,
            "TC028_SMABatchManager_Compressed UPC with Sign",
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
        client.sendText("UPCwithSign")
        time.sleep(2)
        client.sendPF(12)
        time.sleep(2)

        client.saveScreen(file_path, dataType="txt")

        # Comp UPC
        client.sendPF(6)
        time.sleep(2)
        client.saveScreen(file_path, dataType="txt")

        # Provide Compressed UPC
        client.sendText("285652")
        time.sleep(2)
        client.saveScreen(file_path, dataType="txt")

        # Accept
        client.sendPF(12)
        time.sleep(2)
        client.saveScreen(file_path, dataType="txt")

        # Accept
        client.sendPF(12)
        time.sleep(2)
        client.saveScreen(file_path, dataType="txt")

        # Provide Tag/Sign
        client.sendKeys("s")
        time.sleep(2)
        client.saveScreen(file_path, dataType="txt")

        # Process
        client.sendPF(12)
        time.sleep(2)
        client.saveScreen(file_path, dataType="txt")

        # Save
        client.sendPF(12)
        time.sleep(2)
        client.saveScreen(file_path, dataType="txt")

        print("<-------------------Test Case 28 executed------------------->")

    else:
        print("Mainframe Connection Failed.")

    client.disconnect()
    print("Mainframe Disconnected.")
