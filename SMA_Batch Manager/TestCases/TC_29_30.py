import time

from p3270.p3270 import P3270Client

from .utils import add_heading
from .Login import Login


def test_case_29_30(client: P3270Client, username, password):
    # SMABatchManager_View Batch Detail/SMABatchManager_Exit from Detail BatchReviewScreen_To manual batch create
    if client.connect():
        print("Mainframe Connection Successful.")
        time.sleep(7)

        file_path = "Reports/TC_29_30_Report.html"
        add_heading(
            file_path,
            "TC029_30_SMABatchManager_View Batch Detail/SMABatchManager_Exit from Detail BatchReviewScreen_To manual batch create",
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
        client.sendText("batchexit")
        time.sleep(2)
        client.sendPF(12)
        time.sleep(2)

        client.saveScreen(file_path, dataType="txt")

        # Enter UPC
        client.sendText("00002820000565")
        client.sendEnter()
        time.sleep(2)
        # client.saveScreen(file_path, dataType="txt")

        # Provide Tag/Sign
        client.sendKeys("t")
        time.sleep(2)
        # client.saveScreen(file_path, dataType="txt")

        # Process
        client.sendPF(12)
        time.sleep(2)
        client.saveScreen(file_path, dataType="txt")

        # View Batch Detail
        client.sendPF(10)
        time.sleep(2)
        client.saveScreen(file_path, dataType="txt")

        # Exit from Detail Batch Review Screen to Manual Batch Create
        client.sendPF(3)
        time.sleep(2)
        client.saveScreen(file_path, dataType="txt")

        # Process
        client.sendPF(12)
        time.sleep(2)
        client.saveScreen(file_path, dataType="txt")

        print("<-------------------Test Case 29_30 executed------------------->")

    else:
        print("Mainframe Connection Failed.")

    client.disconnect()
    print("Mainframe Disconnected.")
