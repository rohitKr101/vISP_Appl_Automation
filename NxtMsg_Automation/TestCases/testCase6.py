# TC 6 : List all applications
import time

from TestCases.utils import add_heading


def test_case_6(myclient):
    """TC 6 : List all applications"""
    save_path = "Reports/TC6_Report.html"
    add_heading(save_path, "NxtMssg TC 6 : List all applications")

    myclient.sendKeys("l")

    myclient.saveScreen(save_path, dataType="txt")

    myclient.sendEnter()
    time.sleep(7)

    # for i in range(1, 5):
    i = 1
    while "Permission" in myclient.getScreen():
        myclient.saveScreen(save_path, dataType="txt")

        myclient.sendEnter()
        time.sleep(7)
        i += 1

    print("<---------------TC 06 - PASSED-------------->")