import time

from .utils import add_heading
from .Login import Login


def test_case_19(client, username, password):
    # SMABatchManager_Update Quantity for a single batch line_store with multiple batch lines
    if client.connect():
        print("Mainframe Connection Successful.")
        time.sleep(7)

        file_path = "Reports/TC_19_Report.html"
        # list of tuples : (UPC , no. steps to choose the required tag)
        tupleList = [("4011", 3), ("4011", 1), ("4012", 2)]
        add_heading(
            file_path,
            "TC_19_SMABatchManager_Update Quantity for a single batch line_store with multiple batch lines",
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
        client.sendText("Multiple Batch Lines single prt qty")
        time.sleep(2)
        client.saveScreen(file_path, dataType="txt")
        client.sendPF(12)
        time.sleep(2)

        # Add multiple batch lines
        for i, (upc, tag) in enumerate(tupleList):
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

            # Press Enter only if this is NOT the last item
            if i < len(tupleList) - 1:
                client.sendEnter()
                time.sleep(2)

        # Update Quantity for a single batch line
        # client.moveCursorUp()
        # time.sleep(2)

        client.sendText("3")
        time.sleep(2)

        client.saveScreen(file_path, dataType="txt")

        client.sendPF(12)
        time.sleep(2)

        client.saveScreen(file_path, dataType="txt")

        print("<-------------------Test Case 19 executed------------------->")

    else:
        print("Mainframe Connection Failed.")

    client.disconnect()
    print("Mainframe Disconnected.")
