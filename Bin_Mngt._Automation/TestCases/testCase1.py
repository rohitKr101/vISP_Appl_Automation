import time
from TestCases.Login import login
from TestCases.utils import add_heading, add_image


def test_case_1(my_client, username, password):
    """Check SMA Version"""
    save_path = "Reports/Bin_mngt_report.html"

    add_heading(
        save_path,
        "Test Case: BIN Management_Linux:  TC003_T2_LNX_BIN_Management_File exists on A0036946",
    )

    my_client.sendText("sudo /bin/su - sma_user")
    my_client.sendEnter()
    time.sleep(5)

    add_heading(save_path, "Check SMA Version before test")
    my_client.sendText("cd /opt/sma/scripts")
    my_client.sendEnter()
    time.sleep(2)
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
    add_heading(
        save_path,
        "Verify if bank .dat file is present in /opt/sma/transfer_files location",
    )

    my_client.sendText("cd /opt/sma/transfer_files")
    my_client.sendEnter()
    my_client.sendText("ls -lrt")
    time.sleep(2)
    my_client.saveScreen(save_path, dataType="txt")

    my_client.sendEnter()
    time.sleep(2)
    my_client.saveScreen(save_path, dataType="txt")  # can be commented

    """Step 2: Verify that the file is archieved (format : MMDDHHMM.bnk)"""
    add_heading(
        save_path,
        "Verify that the file is archived to /opt/sma/transfer_files/archive directory with the file name format as MMDDHHMM.bnk",
    )
    my_client.sendText("cd /opt/sma/transfer_files/archive")
    my_client.sendEnter()
    my_client.sendText("ls -lrt")
    my_client.sendEnter()
    time.sleep(2)
    my_client.saveScreen(save_path, dataType="txt")

    """Step 3: Verify log file"""
    add_heading(
        save_path,
        "Verify log file ace_bnk_sftp.log in /opt/sma/log/Mon file for archive",
    )
    my_client.sendText("cd /opt/sma/log")
    my_client.sendEnter()
    my_client.sendText("ls -lrt")
    my_client.sendEnter()
    time.sleep(2)
    my_client.saveScreen(save_path, dataType="txt")

    """Step 4: More on Log file"""
    my_client.sendText("more ace_bnk_sftp.log")
    my_client.sendEnter()
    time.sleep(2)
    for _ in range(4):
        my_client.sendEnter()
        time.sleep(1)
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
