import time
from .utils import add_heading
from .Login import Login


def test_case_2(client, username, password):
    # SMA_BatchManager_Batch Creation_Create Batch Header

    if client.connect():
        print("Mainframe Connection Successful.")
        time.sleep(7)

        file_path = "Reports/TC_02_Report.html"
        add_heading(
            file_path, "TC_02_SMA_BatchManager_Batch Creation_Create Batch Header"
        )
        LOGIN = Login(client, username, password)
        LOGIN.login()

        client.sendText("sudo /bin/su - g06949cp1")
        client.sendEnter()
        time.sleep(2)

        client.sendKeys("s")
        time.sleep(2)

        client.saveScreen(file_path, dataType="txt")

        client.sendEnter()
        time.sleep(2)

        client.saveScreen(file_path, dataType="txt")

        client.sendEnter()
        time.sleep(2)

        client.sendKeys("b")
        time.sleep(2)

        client.saveScreen(file_path, dataType="txt")

        client.sendEnter()
        time.sleep(2)

        client.sendText("batch 01")
        time.sleep(2)

        client.saveScreen(file_path, dataType="txt")

        client.sendPF(12)
        time.sleep(2)

        client.saveScreen(file_path, dataType="txt")

        print("<-------------------Test Case 2 executed------------------->")

    else:
        print("Mainframe Connection Failed.")

    client.disconnect()
    print("Mainframe Disconnected.")
