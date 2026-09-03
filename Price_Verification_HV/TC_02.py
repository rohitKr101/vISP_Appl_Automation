    
import time
from utils import add_heading


def testCase_2(my_client, save_path):
    
    add_heading(save_path, "TC02- SMAPriceVerification_Exit from PV Main Menu")
    my_client.sendKeys("b")
    time.sleep(2)
    add_heading(save_path, "Press 'B' to Exit")
    my_client.saveScreen(save_path, dataType="txt")