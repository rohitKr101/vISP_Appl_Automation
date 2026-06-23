import time
from TestCases.utils import add_heading


def test_case_1(my_client):
    """TC 1 : Check successful login"""
    save_path = "Reports/TC1_Report.html"
    add_heading(save_path, "NxtMssg TC 1 : Check successful login")
    my_client.saveScreen(save_path, dataType="txt")

    print("sudo Command Entered")
    my_client.sendEnter()
    time.sleep(2)

    tc1_condition = "0969" in my_client.getScreen()
    print(f"Home Screen Visible : {tc1_condition}")
    if tc1_condition:
        my_client.saveScreen(save_path, dataType="txt")
        print("<---------------TC 01 - PASSED-------------->")
    else:
        print("<---------------TC 01 - FAILED-------------->")
