import datetime
from google.oauth2 import service_account
from googleapiclient.discovery import build
from dateutil import parser
from dateutil import tz

def calculate_hours(start, end):
    print(f"start: {start}, end: {end}")
    if start < end:
        delta = end - start
        return delta.total_seconds() / 3600
    else:
        # The end time is on the next day
        midnight = datetime.datetime.combine(start.date(), datetime.time(0, 0, 0)).replace(tzinfo=start.tzinfo)
        delta1 = midnight - start
        delta2 = end - midnight
        return (delta1.total_seconds() + delta2.total_seconds()) / 3600





def return_time_availability(events, period=1):
    output = {}
    start_time = datetime.time(8, 0, 0)
    end_time = datetime.time(20, 0, 0)

    # Define the date range for analysis (e.g., the next 10 days)
    start_date = datetime.date.today()
    end_date = start_date + datetime.timedelta(days=period)

    # Define the timezone for your local timezone (CST)
    local_tz = tz.gettz('America/Chicago')

    # Iterate through the date range and calculate free hours
    current_date = start_date
    while current_date <= end_date:
        overlap_hours = 0
        # Define the datetime range for the analysis day in local timezone (CST)
        start_datetime_local = datetime.datetime.combine(current_date, start_time).replace(tzinfo=local_tz)
        end_datetime_local = datetime.datetime.combine(current_date, end_time).replace(tzinfo=local_tz)

        # Calculate the total free hours for the day
        total_free_hours = calculate_hours(start_datetime_local, end_datetime_local)

        # Subtract the duration of calendar events from total free hours
        for event in events:
            event_start_str = event['start'].get('dateTime') or event['start'].get('date')
            event_start = parser.parse(event_start_str).astimezone(local_tz)
            if event_start.date() == current_date:

                event_end_str = event['end'].get('dateTime') or event['end'].get('date')
                event_end = parser.parse(event_end_str).astimezone(local_tz)

                # Calculate the overlap duration between the event and the analysis window
                overlap_start = max(start_datetime_local, event_start)
                overlap_end = min(end_datetime_local, event_end)
                overlap_hours = calculate_hours(overlap_start, overlap_end)
                print(f"overlap hours: {overlap_hours}")

                # Subtract overlap hours from the total free hours
                total_free_hours -= overlap_hours

        output[current_date] = total_free_hours

        # Move to the next day
        current_date += datetime.timedelta(days=1)
    return output