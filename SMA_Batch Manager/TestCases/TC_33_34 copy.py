import time
from tqdm import tqdm

from django.test import client
from p3270.p3270 import P3270Client

from .utils import add_heading
from .Login import Login


def test_case_33_34(client: P3270Client, username, password):
    # SMABatchManager__Batch Create_F4 Page Up and F2 Page Down
    if client.connect():
        print("Mainframe Connection Successful.")
        BASEELINE_SECONDS = 180  # Set the baseline time in seconds for the progress bar
        with tqdm(
            total=BASEELINE_SECONDS, desc="Running Test Case 33_34", unit="s"
        ) as pbar:

            time.sleep(7)
            pbar.update(7)

            file_path = "Reports/TC_33_34_Report.html"
            add_heading(
                file_path,
                "TC33_34 SMABatchManager__Batch Create_F4 Page Up and F2 Page Down",
            )
            LOGIN = Login(client, username, password)
            LOGIN.login()

            client.sendText("sudo /bin/su - g06949cp1")
            client.sendEnter()
            time.sleep(2)
            pbar.update(2)

            # Select Shelf Management Systems
            client.sendKeys("s")
            time.sleep(2)
            pbar.update(2)
            client.sendEnter()
            time.sleep(2)
            pbar.update(2)

            # Select Store Batch Manager
            client.sendEnter()
            time.sleep(2)
            pbar.update(2)

            # Select Batch Create
            client.sendKeys("b")
            time.sleep(2)
            pbar.update(2)
            client.saveScreen(file_path, dataType="txt")
            client.sendEnter()
            time.sleep(2)
            pbar.update(2)
            client.sendText("pageupdown")
            time.sleep(2)
            pbar.update(2)
            client.sendPF(12)
            time.sleep(2)
            pbar.update(2)

            client.saveScreen(file_path, dataType="txt")

            for _ in range(15):
                # Enter UPC
                client.sendText("4012")
                client.sendEnter()
                time.sleep(2)
                pbar.update(2)
                # client.saveScreen(file_path, dataType="txt")

                client.sendTab()
                time.sleep(2)
                pbar.update(2)

                # Provide Tag/Sign
                client.sendKeys("t")
                time.sleep(2)
                pbar.update(2)
                # client.saveScreen(file_path, dataType="txt")

                # List all Tag/sign
                if "UNKNOWN" in client.getScreen():
                    client.sendPF(5)
                    time.sleep(2)
                    pbar.update(2)
                    for _ in range(3):  # Select required tag/sign from the list
                        client.sendTab()
                        time.sleep(2)
                        pbar.update(2)
                    # client.saveScreen(file_path, dataType="txt")

                    # Process
                    client.sendPF(12)
                    time.sleep(2)
                    pbar.update(2)
                    # client.saveScreen(file_path, dataType="txt")

                # Process
                client.sendPF(12)
                time.sleep(2)
                pbar.update(2)

                client.sendEnter()
                time.sleep(2)
                pbar.update(2)

            client.saveScreen(file_path, dataType="txt")

            # Press F4 to Page Up
            while "On first page" not in client.getScreen():
                client.sendPF(4)
                time.sleep(2)
                pbar.update(2)
            client.saveScreen(file_path, dataType="txt")

            # Press F2 to Page Down
            while "On last page" not in client.getScreen():
                client.sendPF(2)
                time.sleep(2)
                pbar.update(2)
            client.saveScreen(file_path, dataType="txt")

        print("<-------------------Test Case 33_34 executed------------------->")

    else:
        print("Mainframe Connection Failed.")

    client.disconnect()
    print("Mainframe Disconnected.")
