import time
from TestCases.utils import add_heading


def test_case_5(my_client):
    """TC 5 : Check Daemon Status"""
    save_path = "Reports/TC5_Report.html"
    add_heading(save_path, "NxtMssg TC 5 : Check Daemon Status")
    my_client.sendKeys("c")

    my_client.saveScreen(save_path, dataType="txt")

    my_client.sendEnter()
    time.sleep(7)

    tc5_condition = (
        "Checking communication to POS (a9999cc1)" in my_client.getScreen()
        and "PING FAILED!" not in my_client.getScreen()
    )
    print("Daemon Status : ", tc5_condition)
    if tc5_condition:
        my_client.saveScreen(save_path, dataType="txt")

        print("<---------------TC 05 - PASSED-------------->")
    else:
        my_client.printScreen()
        print("<---------------TC 05 - FAILED-------------->")

    my_client.sendEnter()
    time.sleep(7)
