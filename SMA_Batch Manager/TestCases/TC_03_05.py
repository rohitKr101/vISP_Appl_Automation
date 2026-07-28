import time
from .utils import add_heading
from .Login import Login


def test_case_3_5(client, username, password):
    # SMABatchManager_Batch Creation_Create Store Batch line using UPC number with Tag

    if client.connect():
        print("Mainframe Connection Successful.")
        time.sleep(7)

        file_path = "Reports/TC_03_05_Report.html"
        add_heading(
            file_path,
            "TC_03_05_SMA_BatchManager_Batch Creation_Create Store Batch line using UPC number with Tag",
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

        client.sendText("batch 02")
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

        client.sendKeys("t")
        time.sleep(2)

        client.saveScreen(file_path, dataType="txt")

        client.sendPF(5)
        time.sleep(2)

        # No. of tabs to choose the tag
        for _ in range(3):
            client.sendTab()
            time.sleep(2)

        client.saveScreen(file_path, dataType="txt")

        client.sendPF(12)
        time.sleep(2)

        client.saveScreen(file_path, dataType="txt")

        client.sendPF(12)
        time.sleep(2)

        client.saveScreen(file_path, dataType="txt")

        print("<-------------------Test Case 3 and 5 executed------------------->")

    else:
        print("Mainframe Connection Failed.")

    client.disconnect()
    print("Mainframe Disconnected.")
