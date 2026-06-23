import os
import time
from dotenv import load_dotenv
from p3270 import P3270Client

from TestCases.testCase1 import test_case_1
from TestCases.testCase2 import test_case_2
from TestCases.testCase3 import test_case_3
from TestCases.testCase4 import test_case_4
from TestCases.testCase5 import test_case_5
from TestCases.testCase6 import test_case_6
from TestCases.testCase7 import test_case_7
from TestCases.testCase8 import test_case_8
from TestCases.testCase9 import test_case_9
from TestCases.testCase10 import test_case_10

load_dotenv(
    override=True
)  # load the .env file and override existing system environment variables if they exist

Hostname = os.getenv("HOSTNAME")
Username = os.getenv("USERNAME")
Password = os.getenv("PASSWORD")


def main():
    my_client = P3270Client(hostName=Hostname)

    if my_client.connect():
        print("Mainframe Connection Successful.")
        time.sleep(7)

        my_client.sendEnter()
        time.sleep(7)
        my_client.sendText(Username)
        my_client.sendEnter()
        print("Username Entered")
        time.sleep(7)

        my_client.moveTo(15, 11)
        my_client.sendText(Password)
        my_client.sendEnter()
        print("Password Entered")
        time.sleep(7)

        my_client.sendText("export TERM=xterm")
        my_client.sendEnter()
        time.sleep(2)

        my_client.sendText("sudo /bin/su - nextmsgr")
        time.sleep(6)

        """Uncomment when individual test cases need to be run"""
        # my_client.sendEnter()
        # time.sleep(2)

        # TC 1 : Check successful login
        test_case_1(my_client)

        # TC 2 : Validate 8 Options
        test_case_2(my_client)

        # TC 3 : Check Start Daemon Status
        test_case_3(my_client)

        # TC 4 : Check Stop Daemon Status
        test_case_4(my_client)

        # TC 5 : Check Daemon Status
        test_case_5(my_client)

        # TC 6 : List all applications
        test_case_6(my_client)

        # TC 7 : Review POS to WEb log file
        test_case_7(my_client)

        # TC 8 : Review WEB to POS log file
        test_case_8(my_client)

        # TC 9 : Review POS to WEB control file
        test_case_9(my_client)

        # TC 10 : Review WEB to POS control file
        test_case_10(my_client)

    else:
        print("Mainframe Connection Failed.")

    my_client.disconnect()
    print("Mainframe Disconnected.")


if __name__ == "__main__":
    main()
