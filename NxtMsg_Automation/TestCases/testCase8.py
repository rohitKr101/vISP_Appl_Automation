# TC 8 : Review WEB to POS log file
import time

from TestCases.utils import add_heading


def test_case_8(my_client):
    """TC 8 : Review WEB to POS log file"""
    save_path = "Reports/TC8_Report.html"
    add_heading(save_path, "NxtMssg TC 8 : Review WEB to POS log file")
    # for _ in range(2):
    #     self.my_client.sendKeys("r")
    #     time.sleep(0.1)

    my_client.sendKeys("r")

    my_client.saveScreen(save_path, dataType="txt")

    my_client.sendEnter()
    time.sleep(7)

    for _ in range(30):
        my_client.sendEnter()
    my_client.saveScreen(save_path, dataType="txt")

    my_client.sendKeys("G")
    time.sleep(7)

    my_client.saveScreen(save_path, dataType="txt")
    my_client.sendKeys("q")
    time.sleep(7)
    print("<---------------TC 08 - PASSED-------------->")
