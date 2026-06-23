import time
from TestCases.Login import login
from TestCases.utils import add_heading


def test_case_1(my_client, username, password):
    """Check SMA Version"""
    login(my_client, username, password)
    save_path = "Reports/Bin_mngt_report.html"

    my_client.sendText("sudo /bin/su - sma_user")
    my_client.sendEnter()
    time.sleep(5)

    add_heading(save_path, "Check SMA Version before test")
    my_client.sendText("cd /opt/sma/scripts")
    my_client.sendEnter()
    my_client.sendText("ls -lrt post*")
    time.sleep(5)

    my_client.saveScreen(save_path, dataType="txt")
    my_client.sendEnter()
    time.sleep(7)

    my_client.saveScreen(save_path, dataType="txt")

    my_client.disconnect()
    print("Mainframe Disconnected")

    """Step1 : Verify if .dat file exists"""
    login(my_client, username, password)
    add_heading(save_path, "Check if .dat file exists")

    my_client.sendText("cd /opt/sma/transfer_files")
    my_client.sendEnter()
    my_client.sendText("ls -lrt")
    time.sleep(2)
    my_client.saveScreen(save_path, dataType="txt")

    my_client.sendEnter()
    time.sleep(2)
    my_client.saveScreen(save_path, dataType="txt")  # can be commented

    """Step 2: Verify that the file is archieved (format : MMDDHHMM.bnk)"""
    add_heading(save_path, "Verify that the file is archived with correct format")
    my_client.sendText("cd /opt/sma/transfer_files/archive")
    my_client.sendEnter()
    my_client.sendText("ls -lrt")
    my_client.sendEnter()
    time.sleep(2)
    my_client.saveScreen(save_path, dataType="txt")

    """Step 3: Verify log file"""
    add_heading(save_path, "Verify log file ace_bnk_sftp.log")
    my_client.sendText("cd /opt/sma/log/sat")
    my_client.sendEnter()
    my_client.sendText("ls -lrt")
    my_client.sendEnter()
    time.sleep(2)
    my_client.saveScreen(save_path, dataType="txt")

    """Step 4: More on Log file"""
    my_client.sendText("more ace_bnk_sftp.log")
    my_client.sendEnter()
    time.sleep(2)
    my_client.saveScreen(save_path, dataType="txt")

    """Step 5: Check SMA Version"""
    add_heading(save_path, "Check SMA Version after test")
    my_client.sendText("cd /opt/sma/scripts")
    my_client.sendEnter()
    my_client.sendText("ls -lrt")
    my_client.sendEnter()
    time.sleep(7)
    my_client.saveScreen(save_path, dataType="txt")

    my_client.disconnect()
    print("Mainframe Disconnected")
