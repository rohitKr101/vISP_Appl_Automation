import time

from TestCases.Login import Login
from .utils import add_heading


def test_case_3(my_client, username, password):
    """Test Case 3: Check ge_item extract and logs (Run after ControlM has completed the Job Status)"""
    save_path = "Reports/SMA_GEPS_TC3.html"
    add_heading(save_path, "SMA Great Entertaining Price Support")
    add_heading(save_path, "TC3: Run run_posim.K on ad break day (Friday)")
    login = Login(my_client, username, password)
    login.login()

    add_heading(save_path, "1. Login to lab box 6949 and enter SUDO command.")
    my_client.saveScreen(save_path, dataType="txt")

    my_client.sendText("sudo /bin/su - sma_user")
    my_client.sendEnter()
    time.sleep(5)
    my_client.saveScreen(save_path, dataType="txt")

    my_client.sendText("cd /opt/sma/transfer_files")
    my_client.sendEnter()
    time.sleep(2)
    my_client.sendText("ls -lrt")
    my_client.sendEnter()
    time.sleep(2)
    add_heading(
        save_path,
        "2. Go to /opt/sma/transfer_files and check if geupcs.txt is present.",
    )
    my_client.saveScreen(save_path, dataType="txt")

    my_client.sendText("cd /opt/sma/transfer_files/out")
    my_client.sendEnter()
    time.sleep(2)

    my_client.sendText("ls -lrt ge_item*")
    my_client.sendEnter()
    time.sleep(2)
    add_heading(
        save_path,
        "3. Navigate to /opt/sma/transfer_files/out and check if the ge_item_extract.txt file is present in the path",
    )
    my_client.saveScreen(save_path, dataType="txt")

    my_client.sendText("tail -10 ge_item_extract.txt")
    my_client.sendEnter()
    time.sleep(2)
    my_client.saveScreen(save_path, dataType="txt")

    my_client.sendText("cd /opt/sma/log")
    my_client.sendEnter()
    time.sleep(2)

    my_client.sendText("ls -lrt ge_item*")
    my_client.sendEnter()
    time.sleep(2)
    add_heading(
        save_path,
        "4. Navigate to /opt/sma/log and check if the ge_item_extract.log file is present in the path; validate success message in log file ",
    )
    my_client.saveScreen(save_path, dataType="txt")

    my_client.sendText("tail -4 ge_item_extract.log")
    my_client.sendEnter()
    time.sleep(2)
    my_client.saveScreen(save_path, dataType="txt")

    print("<---------------TC 03 - Executed-------------->")
