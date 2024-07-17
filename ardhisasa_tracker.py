import os
import requests
import pandas as pd
from datetime import datetime
import pywhatkit

# Variables
sheet_id = ""
sheet_gid = ""
destination = "deployments_and_demos.csv"

mode = "contact"

phone_numer = ''
group_id = ''
message = 'Write the message here'

waiting_time_to_send = 10
close_tab = True
waiting_time_to_close = 2

time_hour = 12
time_minute = 21



def download_google_sheet_as_csv(sheet_id, sheet_gid, destination):
    url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv&gid={sheet_gid}"
    response = requests.get(url)
    response.raise_for_status()  # Ensure we notice bad responses
    with open(destination, 'wb') as f:
        f.write(response.content)

def get_last_three_entries_from_csv(file_path):
    df = pd.read_csv(file_path)
    df.columns = df.columns.str.strip()  # Strip any leading/trailing whitespace from columns
    last_three_entries = df.tail(3)
    return last_three_entries

def format_entries(entries):
    current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    updates = [f"The following are the updates as of today {current_datetime};"]
    for _, row in entries.iterrows():
        process = row["Process"]
        training_date = row["Training"]
        live_date = row["Live"]
        
        if pd.isna(training_date) and pd.isna(live_date):
            update = f"- {process} has no deployments to the Training or Live environments."
        elif pd.isna(training_date):
            update = f"- {process} was deployed to the Live environment on {live_date}."
        elif pd.isna(live_date):
            update = f"- {process} was deployed to the Training environment on {training_date}."
        else:
            update = (
                f"- {process} was deployed to the Training environment on {training_date} "
                f"and to the Live environment on {live_date}."
            )
        updates.append(update)
    return "\n".join(updates)

def main():

    # Calculate current time
    current_time = datetime.now()

     # Set time_hour to current hour
    time_hour = current_time.hour

    # Set time_minute to 10 minutes after the current minute
    time_minute = (current_time.minute + 5) % 60

    # Download the Google Sheet as a CSV file
    download_google_sheet_as_csv(sheet_id, sheet_gid, destination)

    # Process the CSV file to get the last three entries
    last_three_entries = get_last_three_entries_from_csv(destination)

    # Format and print the entries
    formatted_entries = format_entries(last_three_entries)
    message = formatted_entries

    print(message)

    if mode == "contact":
        # Send a WhastApp message to an specific contact
        pywhatkit.sendwhatmsg(phone_numer, message, time_hour, time_minute, waiting_time_to_send, close_tab, waiting_time_to_close)
    elif mode == "group":
        # Send a WhastApp message to an specific group
        pywhatkit.sendwhatmsg_to_group(group_id, message, time_hour, time_minute, waiting_time_to_send, close_tab, waiting_time_to_close)
    else:
        print("Error code: 97654")
        print("Error Message: Please select a mode to send your message.")

    # Delete the downloaded file
    os.remove(destination)

if __name__ == "__main__":
    main()
