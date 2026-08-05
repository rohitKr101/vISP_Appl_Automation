import time

from .utils import add_heading
from .Login import Login


def test_case_9_11(client, username, password):
    # SMABatchManager_Batch Creation_Create Store Batch line using  Item Number and Sign_End to End flow

    if client.connect():
        print("Mainframe Connection Successful.")
        time.sleep(7)

        file_path = "Reports/TC_09_11_Report.html"
        add_heading(
            file_path,
            "TC_09_11_SMABatchManager_Batch Creation_Create Store Batch line using  Item Number and Sign_End to End flow",
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

        client.sendText("item Create")
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

        client.sendText("2")
        time.sleep(2)

        client.sendPF(12)
        time.sleep(2)

        client.saveScreen(file_path, dataType="txt")

        print("<-------------------Test Case 9 and 11 executed------------------->")

    else:
        print("Mainframe Connection Failed.")

    client.disconnect()
    print("Mainframe Disconnected.")
