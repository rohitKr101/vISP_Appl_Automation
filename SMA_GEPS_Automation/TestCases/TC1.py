# # Add parent directory to path to import Login
# sys.path.insert(0, str(Path(__file__).parent.parent))

import time

from TestCases.Login import Login
from .utils import add_heading


def test_case_1(my_client, username, password):
    """Test Case 1: Initial login and setup"""
    save_path = "Reports/SMA_GEPS_TC1.html"
    add_heading(save_path, "SMA Great Entertaining Price Support")
    add_heading(save_path, "TC 1: Check Availability of geupcs.txt file.")
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
    add_heading(save_path, "2. Go to /opt/sma/transfer_files and check if geupcs.txt is present.")
    my_client.saveScreen(save_path, dataType="txt")

    print("<---------------TC 01 - Executed-------------->")
