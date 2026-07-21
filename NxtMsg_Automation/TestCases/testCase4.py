import time
from TestCases.utils import add_heading


def test_case_4(my_client):
    """TC 4 : Check Stop Daemon Status"""
    save_path = "Reports/TC4_Report.html"
    add_heading(save_path, "NxtMssg TC 4 : Check Stop Daemon Status")
    my_client.sendKeys("s")

    my_client.saveScreen(save_path, dataType="txt")

    my_client.sendEnter()
    time.sleep(7)

    tc4_condition = "still running." in my_client.getScreen()
    print("Stop Daemon Status : ", tc4_condition)

    if tc4_condition:
        my_client.saveScreen(save_path, dataType="txt")

        print("<---------------TC 04 - PASSED-------------->")
    else:
        my_client.printScreen()
        print("<---------------TC 04 - FAILED-------------->")

    my_client.sendEnter()
    time.sleep(7)
