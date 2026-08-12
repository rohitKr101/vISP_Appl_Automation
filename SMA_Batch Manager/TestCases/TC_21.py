import time

from .utils import add_heading
from .Login import Login


def test_case_21(client, username, password):
    # SMABatchManager_Vendor Search_By vendor number
    if client.connect():
        print("Mainframe Connection Successful.")
        time.sleep(7)

        file_path = "Reports/TC_21_Report.html"
        add_heading(
            file_path,
            "TC_21_SMABatchManager_Vendor Search_By vendor number",
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

        # Add Vendor Number
        client.sendText("1306")
        client.sendEnter()
        time.sleep(2)
        client.saveScreen(file_path, dataType="txt")

        client.sendPF(12)
        time.sleep(2)
        client.saveScreen(file_path, dataType="txt")

        # Select Tag
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

        # Add quantity
        client.sendText("2")
        time.sleep(2)
        client.sendPF(12)
        time.sleep(2)
        client.saveScreen(file_path, dataType="txt")

        print("<-------------------Test Case 21 executed------------------->")

    else:
        print("Mainframe Connection Failed.")

    client.disconnect()
    print("Mainframe Disconnected.")
