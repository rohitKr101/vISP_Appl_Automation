import time
from TestCases.utils import add_heading


def test_case_3(my_client):
    """TC 3 : Check Start Daemon Status"""
    save_path = "Reports/TC3_Report.html"
    add_heading(save_path, "NxtMssg TC 3 : Check Start Daemon Status")

    my_client.saveScreen(save_path, dataType="txt")

    my_client.sendEnter()
    time.sleep(5)
    my_client.sendEnter()
    time.sleep(7)

    tc3_condition = "still running." in my_client.getScreen()
    print("Start Daemon Status : ", tc3_condition)

    if tc3_condition:
        my_client.saveScreen(save_path, dataType="txt")

        print("<---------------TC 03 - PASSED-------------->")
    else:
        my_client.printScreen()
        print("<---------------TC 03 - FAILED-------------->")

    time.sleep(7)
