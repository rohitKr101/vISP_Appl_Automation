import time
from utils import add_heading


def testCase_1(my_client, save_path):

    add_heading(
        save_path,
        "TC01- SMAPriceVerification_Login to PV application_Direct Audit Mode_through pvhh.pl",
    )
    add_heading(save_path, "Login to Lab 6978 and do sudo to su_sma_user")
    my_client.sendText("sudo /bin/su - sma_user")
    my_client.sendEnter()
    time.sleep(5)
    my_client.saveScreen(save_path, dataType="txt")

    my_client.sendText("cd /opt/sma/pv/HH")
    my_client.sendEnter()
    time.sleep(2)
    my_client.sendText("pvhh.pl")
    time.sleep(2)
    add_heading(save_path, "Go to /opt/sma/pv/HH and run pvhh.pl")
    my_client.saveScreen(save_path, dataType="txt")

    my_client.sendEnter()
    time.sleep(2)
    add_heading(save_path, "PV Direct Audit mode opens up. Press Enter.")
    my_client.saveScreen(save_path, dataType="txt")

    my_client.sendEnter()
    time.sleep(2)
    add_heading(save_path, "PV1 screen opens")
    my_client.saveScreen(save_path, dataType="txt")

    my_client.sendText("4011")
    my_client.sendEnter()
    time.sleep(2)
    add_heading(save_path, "Enter UPC")
    my_client.saveScreen(save_path, dataType="txt")
