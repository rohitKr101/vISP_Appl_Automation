import time
from TestCases.Login import Login
from .utils import add_heading


def test_case_4(my_client, username, password):
    """Test Case 4: Check common and transfer files (Run after ControlM has completed the Job Status)"""
    save_path = "Reports/SMA_GEPS_TC4.html"
    add_heading(save_path, "SMA Great Entertaining Price Support")
    add_heading(
        save_path, "TC 4: Verify results of Autosys job a_6946_sma_REQ_ge_item_extract"
    )
    login = Login(my_client, username, password)
    login.login()

    add_heading(save_path, "1. Login to lab box 6946 and enter SUDO command.")
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

    my_client.sendEnter()
    my_client.sendEnter()
    my_client.sendText("cd /opt/sma/sbm/common")
    my_client.sendEnter()
    time.sleep(2)

    my_client.sendText("ls -lrt")
    my_client.sendEnter()
    time.sleep(2)
    add_heading(
        save_path,
        "3. Validated sbm.ini file is present in /opt/sma/sbm/common folder",
    )
    my_client.saveScreen(save_path, dataType="txt")

    my_client.sendEnter()
    my_client.sendEnter()
    my_client.sendText("cd /opt/sma/transfer_files")
    my_client.sendEnter()
    time.sleep(2)
    my_client.sendText("ls -lrt")
    my_client.sendEnter()
    time.sleep(2)
    add_heading(
        save_path, "4. Validated geupcs.txt file in /opt/sma/transfer_files folder."
    )
    my_client.saveScreen(save_path, dataType="txt")

    my_client.sendEnter()
    my_client.sendEnter()
    my_client.sendText("cd /opt/sma/transfer_files/out")
    my_client.sendEnter()
    time.sleep(2)

    my_client.sendText("ls -lrt ge_item*")
    my_client.sendEnter()
    time.sleep(2)
    add_heading(
        save_path,
        "5. To validate if ge_item_extract.log has run successfully.",
    )
    my_client.saveScreen(save_path, dataType="txt")

    my_client.sendEnter()
    my_client.sendEnter()
    my_client.sendText("cd /opt/sma/log")
    my_client.sendEnter()
    time.sleep(2)
    my_client.sendText("ls -lrt ge_item*")
    my_client.sendEnter()
    time.sleep(2)
    my_client.saveScreen(save_path, dataType="txt")

    my_client.sendText("tail -10 ge_item_extract.log")
    my_client.sendEnter()
    time.sleep(2)
    my_client.saveScreen(save_path, dataType="txt")

    print("<---------------TC 04 - Executed-------------->")
