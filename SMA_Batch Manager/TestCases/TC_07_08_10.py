import time

from django.test import client
from .utils import add_heading
from .Login import Login


def test_case_7_8_10(client, username, password):
    # SMABatchManager_Batch Creation_Create Store Batch line using  Item Number, With  Tag _End to End flow

    if client.connect():
        print("Mainframe Connection Successful.")
        time.sleep(7)

        file_path = "Reports/TC_07_08_10_Report.html"
        add_heading(
            file_path,
            "TC_07_08_10_SMA_BatchManager_Batch Creation_Create Store Batch line using Item Number and Tag",
        )
        LOGIN = Login(client, username, password)
        LOGIN.login()

        client.sendText("sudo /bin/su - g06949cp1")
        client.sendEnter()
        time.sleep(2)

        client.sendKeys("s")
        time.sleep(2)

        client.sendEnter()
        time.sleep(2)

        client.sendEnter()
        time.sleep(2)

        client.sendKeys("b")
        time.sleep(2)

        client.saveScreen(file_path, dataType="txt")

        client.sendEnter()
        time.sleep(2)

        client.sendText("batch 04")
        time.sleep(2)

        client.saveScreen(file_path, dataType="txt")

        client.sendPF(12)
        time.sleep(3)

        client.sendTab()
        time.sleep(2)

        client.sendText("41110")
        time.sleep(3)

        client.sendEnter()
        time.sleep(2)

        client.saveScreen(file_path, dataType="txt")

        client.sendKeys("t")
        time.sleep(2)

        client.saveScreen(file_path, dataType="txt")

        client.sendPF(5)
        time.sleep(2)

        # No. of tabs to choose the tag
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

        client.sendText("2")
        time.sleep(2)

        client.sendPF(12)
        time.sleep(2)

        client.saveScreen(file_path, dataType="txt")

        print("<-------------------Test Case 7 and 8 executed------------------->")

    else:
        print("Mainframe Connection Failed.")

    client.disconnect()
    print("Mainframe Disconnected.")
