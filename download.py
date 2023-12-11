import schedule
import time
import requests
from datetime import datetime, timedelta
from requests.exceptions import Timeout

def download_file(url, destination):
    # Adding in a try except loop to handle timeouts
    try:
        response = requests.get(url, timeout=45)
        with open(destination, 'wb') as file:
            file.write(response.content)
        print(f"File downloaded from {url} to {destination} at {datetime.now()}")
    except Timeout:
        print("Timed Out, Retrying...")

def download_job():
    # Id and Name correspond to the Automation TDX Test in my drive (rwastell)
    spreadsheet_id = "1MIbWwEQTLTl6QcoD-DrXDLDB7Zxd9PIBhXErPFZuQBU"
    sheet_name = "Output"
    url = 'https://docs.google.com/spreadsheets/d/' + spreadsheet_id + '/export?format=csv&sheet=' + sheet_name
    # Currently stores in the same directory however there is a chance it might be able to access file of "dongle"
    destination_file_path = 'output_file.csv'
    download_file(url, destination_file_path)

# Schedule the download to occur: Need to set a time for it (Google Script only takes about a minute to run).
schedule.every().monday.at('16:44').do(download_job)

# Infinite loop to have download running in background
while True:
    schedule.run_pending()
    time.sleep(1)
