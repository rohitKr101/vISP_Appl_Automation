import time

from TestCases.Login import Login
from .utils import add_heading


def test_case_3(my_client, username, password):
    """Test Case 3: Check ge_item extract and logs (Run after ControlM has completed the Job Status)"""
    save_path = "Reports/SMA_GEPS_TC3.html"
    add_heading(save_path, "SMA_GEPS_Test_Case_3")
    login = Login(my_client, username, password)
    login.login()

    my_client.sendText("cd /opt/sma/transfer_files/out")
    my_client.sendEnter()
    time.sleep(2)

    my_client.sendText("ls -lrt ge_item*")
    my_client.sendEnter()
    time.sleep(2)
    add_heading(save_path, "SMA_GEPS_ge_item_extract")
    my_client.saveScreen(save_path, dataType="txt")

    my_client.sendText("tail -10 ge_item_extract.txt")
    my_client.sendEnter()
    time.sleep(2)
    add_heading(save_path, "SMA_GEPS_tail_output")
    my_client.saveScreen(save_path, dataType="txt")

    my_client.sendText("cd /opt/sma/log")
    my_client.sendEnter()
    time.sleep(2)

    my_client.sendText("ls -lrt ge_item*")
    my_client.sendEnter()
    time.sleep(2)

    my_client.sendText("tail -4 ge_item_extract.log")
    my_client.sendEnter()
    time.sleep(2)
    add_heading(save_path, "SMA_GEPS_log_files")
    my_client.saveScreen(save_path, dataType="txt")
