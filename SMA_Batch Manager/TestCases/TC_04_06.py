import time

from .utils import add_heading
from .Login import Login


def test_case_4_6(client, username, password):
    # SMABatchManager_Batch Creation_Create Store Batch line using UPC number and Sign

    if client.connect():
        print("Mainframe Connection Successful.")
        time.sleep(7)

        file_path = "Reports/TC_04_06_Report.html"
        add_heading(
            file_path,
            "TC_04_06_SMA_BatchManager_Batch Creation_Create Store Batch line using UPC number and Sign",
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

        client.sendText("batch 03")
        time.sleep(2)

        client.saveScreen(file_path, dataType="txt")

        client.sendPF(12)
        time.sleep(3)

        client.sendText("4011")
        time.sleep(3)

        client.sendEnter()
        time.sleep(2)

        client.saveScreen(file_path, dataType="txt")

        client.sendTab()
        time.sleep(2)

        client.sendKeys("s")
        time.sleep(2)

        client.saveScreen(file_path, dataType="txt")

        client.sendPF(5)
        time.sleep(2)

        # No. of tabs to choose the sign
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

        print("<-------------------Test Case 4 and 6 executed------------------->")

    else:
        print("Mainframe Connection Failed.")

    client.disconnect()
    print("Mainframe Disconnected.")
