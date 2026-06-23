import time
from TestCases.utils import add_heading


def test_case_10(my_client):
    """TC 10 : Review WEB to POS control file"""
    save_path = "Reports/TC10_Report.html"
    add_heading(save_path, "NxtMssg TC 10 : Review WEB to POS control file")

    for _ in range(3):
        my_client.sendKeys("r")
        time.sleep(0.1)

    # my_client.sendKeys("r")
    # time.sleep(5)

    my_client.saveScreen(save_path, dataType="txt")

    my_client.sendEnter()
    time.sleep(7)

    my_client.saveScreen(save_path, dataType="txt")

    while "END" not in my_client.getScreen():
        my_client.sendEnter()

    my_client.saveScreen(save_path, dataType="txt")

    my_client.sendKeys("q")
    time.sleep(7)
    print("<---------------TC 10 - PASSED-------------->")
