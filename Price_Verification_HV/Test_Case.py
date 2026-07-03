import time
from Login import login
from utils import add_heading


def testCase1(my_client, Username, Password):
    save_path = "PV_Report.html"

    login(my_client, Username, Password)

    add_heading(save_path, "Login")
    my_client.saveScreen(save_path, dataType="txt")

    my_client.sendText("cd /opt/sma/pv/HH")
    my_client.sendEnter()
    time.sleep(2)
    my_client.sendText("pvhh.pl")
    time.sleep(2)
    add_heading(save_path, "HH Directory")
    my_client.saveScreen(save_path, dataType="txt")

    my_client.sendEnter()
    time.sleep(2)
    add_heading(save_path, "HH Script")
    my_client.saveScreen(save_path, dataType="txt")

    my_client.sendEnter()
    time.sleep(2)
    add_heading(save_path, "HH Output")
    my_client.saveScreen(save_path, dataType="txt")

    my_client.sendText("4011")
    my_client.sendEnter()
    time.sleep(2)
    add_heading(save_path, "4011 Output")
    my_client.saveScreen(save_path, dataType="txt")

    my_client.sendKeys("b")
    time.sleep(2)
    add_heading(save_path, "Sign-off")
    my_client.saveScreen(save_path, dataType="txt")
