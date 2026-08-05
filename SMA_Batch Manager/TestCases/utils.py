from datetime import datetime
import time


def add_heading(file_name, heading):
    """Add an HTML heading to a file"""
    with open(file_name, "a") as f:
        f.write(
            f"<h2 style='background: rgb(0 0 0 / 88%);border-left: 20px solid #C62828;box-shadow: rgb(202, 201, 201) 0px 2px 10px 0px;color: #008000;font-size: 18px;font-weight: 600;line-height: 1.7em;padding: 10px;text-align: center;user-select: none;border-radius: 10px;'>{heading}</h2>\n"
        )


def fetch_ExpectedDate(client, file_path):
    # Fetch the expected date from the mainframe screen
    today = datetime.today()

    # IST date and time
    mmdate = today.strftime("%m")
    dddate = today.strftime("%d")
    yydate = "20" + today.strftime("%y")

    screen = client.getScreen()
    rows = screen.splitlines()

    print(f"Today: {mmdate}/{dddate}/{yydate}")

    # Search for today's batch
    target_row = None
    batch_count = None

    for row in range(6, 16):

        line = rows[row - 1]

        month = line[15:17].strip()  # Columns 16-17
        day = line[18:20].strip()  # Columns 19-20
        year = line[21:25].strip()  # Columns 22-25

        # Change the condition to match the expected date format
        if month == mmdate and day == dddate and year == yydate:
            target_row = row
            batch_count = line[32:35].strip()  # Columns 33-35
            print(f"Row {row}: {month}/{day}/{year}")
            break

    # If no batch found
    if target_row is None:
        print("Today's batch not found.")
    else:
        print(f"Today's batch found on row {target_row}")
        print(f"Number of items = {batch_count}")

        # Move cursor to target row (Assumes cursor starts on row 6)
        moves = target_row - 6

        for _ in range(moves):
            client.sendTab()
            time.sleep(1)

        # Open the batch
        client.sendPF("12")
        time.sleep(1)

        print("Batch opened successfully.")

    client.saveScreen(file_path, dataType="txt")
