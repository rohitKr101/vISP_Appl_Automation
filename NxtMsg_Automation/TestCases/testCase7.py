# TC 7 : Review POS to WEb log file
import time

from TestCases.utils import add_heading


def test_case_7(my_client):
    """TC 7 : Review POS to WEb log file"""
    save_path = "Reports/TC7_Report.html"
    add_heading(save_path, "NxtMssg TC 7 : Review POS to WEb log file")

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
    print("<---------------TC 07 - PASSED-------------->")
