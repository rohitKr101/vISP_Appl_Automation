import time
from TestCases.Login import Login
from .utils import add_heading


def test_case_2(my_client, username, password):
    """Test Case 2: Check UPC's"""
    save_path = "Reports/SMA_GEPS_TC2.html"
    add_heading(save_path, "SMA_GEPS_Test_Case_2")
    login = Login(my_client, username, password)
    login.login()

    my_client.sendText("cat geupcs.txt")
    time.sleep(2)
    add_heading(save_path, "SMA_GEPS_geupcs_command")
    my_client.saveScreen(save_path, dataType="txt")

    my_client.sendEnter()
    time.sleep(6)
    add_heading(save_path, "SMA_GEPS_UPC's")
    my_client.saveScreen(save_path, dataType="txt")
