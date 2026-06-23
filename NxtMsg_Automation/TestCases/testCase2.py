
from TestCases.utils import add_heading


def test_case_2(my_client):
    """ TC 2 : Validate All Options """
    save_path = "Reports/TC2_Report.html"
    add_heading(save_path, "NxtMssg TC 2 : Validate All Options")

    options = [
        "Start daemon",
        "Stop daemon",
        "Check daemon status",
        "List all application files",
        "Review POS to WEB log file",
        "Review WEB to POS log file",
        "Review POS to WEB control file",
        "Review WEB to POS control file"
    ]

    tc2_condition = all(option in my_client.getScreen() for option in options)
    print("All options available in Home Screen : ", tc2_condition)
    if tc2_condition:
        my_client.saveScreen(save_path, dataType="txt")

        print("<---------------TC 02 - PASSED-------------->")
    else:
        print("<---------------TC 02 - FAILED-------------->")