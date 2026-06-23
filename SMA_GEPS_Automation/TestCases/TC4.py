import time
from TestCases.Login import Login
from .utils import add_heading


def test_case_4(my_client, username, password):
    """Test Case 4: Check common and transfer files (Run after ControlM has completed the Job Status)"""
    save_path = "Reports/SMA_GEPS_TC4.html"
    add_heading(save_path, "SMA_GEPS_Test_Case_4")
    login = Login(my_client, username, password)
    login.login()

    my_client.sendText("cd /opt/sma/common")
    my_client.sendEnter()
    time.sleep(2)

    my_client.sendText("ls -lrt")
    my_client.sendEnter()
    time.sleep(2)
    add_heading(save_path, "SMA_GEPS_common_directory")
    my_client.saveScreen(save_path, dataType="txt")

    my_client.sendText("cd /opt/sma/transfer_files")
    my_client.sendEnter()
    my_client.sendText("ls -lrt")
    my_client.sendEnter()
    time.sleep(2)
    add_heading(save_path, "SMA_GEPS_check_transfer_files")
    my_client.saveScreen(save_path, dataType="txt")

    my_client.sendText("cd /opt/sma/transfer_files/out")
    my_client.sendEnter()
    time.sleep(2)

    my_client.sendText("ls -lrt ge_item*")
    my_client.sendEnter()
    time.sleep(2)
    add_heading(save_path, "SMA_GEPS_check_output_txt")
    my_client.saveScreen(save_path, dataType="txt")

    my_client.sendText("cd /opt/sma/log")
    my_client.sendEnter()

    my_client.sendText("ls -lrt ge_item*")
    my_client.sendEnter()
    time.sleep(2)
    add_heading(save_path, "SMA_GEPS_check_output_log")
    my_client.saveScreen(save_path, dataType="txt")

    my_client.sendText("tail -4 ge_item_extract.log")
    my_client.sendEnter()
    time.sleep(2)
    add_heading(save_path, "SMA_GEPS_check_log_tail")
    my_client.saveScreen(save_path, dataType="txt")
