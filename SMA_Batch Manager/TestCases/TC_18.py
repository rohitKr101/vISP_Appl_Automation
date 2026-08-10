import time

from .utils import add_heading
from .Login import Login


def test_case_18(client, username, password):
    # SMABatchManager_Update quantity_For a batch with multiple batch line
    if client.connect():
        print("Mainframe Connection Successful.")
        time.sleep(7)

        file_path = "Reports/TC_18_Report.html"
        # list of tuples : (UPC , no. steps to choose the required tag)
        tupleList = [
            ("4011", 3),
            ("4011", 1),
            ("4012", 2),
        ]
        add_heading(
            file_path,
            "TC_18_SMABatchManager_Update quantity_For a batch with multiple batch line",
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
        client.sendText("Multiple Batch Lines prt qty")
        time.sleep(2)
        client.saveScreen(file_path, dataType="txt")
        client.sendPF(12)
        time.sleep(2)

        # Add multiple batch lines
        for upc, tag in tupleList:
            # Add UPC
            client.sendText(upc)
            time.sleep(2)
            client.sendEnter()
            time.sleep(2)

            # Select Tag
            client.sendTab()
            time.sleep(2)
            client.sendKeys("t")
            time.sleep(2)

            # List all tags
            client.sendPF(5)
            time.sleep(2)

            # No. of tabs to choose the required tag
            for _ in range(tag):
                client.sendTab()
                time.sleep(1)

            client.sendPF(12)
            time.sleep(2)
            client.sendPF(12)
            time.sleep(2)
            client.saveScreen(file_path, dataType="txt")

            client.sendEnter()
            time.sleep(2)

        # Update Quantity
        client.sendPF(8)
        time.sleep(2)
        client.saveScreen(file_path, dataType="txt")

        client.sendText(3)
        time.sleep(2)
        client.saveScreen(file_path, dataType="txt")

        client.sendPF(12)
        time.sleep(2)
        client.saveScreen(file_path, dataType="txt")

        print("<-------------------Test Case 18 executed------------------->")

    else:
        print("Mainframe Connection Failed.")

    client.disconnect()
    print("Mainframe Disconnected.")
