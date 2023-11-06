from __future__ import print_function

import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly', 'https://www.googleapis.com/auth/tasks']


def create_task_for_user(username, date, task):
    """Shows basic usage of the Tasks API.
    Prints the title and ID of the first 10 task lists.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        service = build('tasks', 'v1', credentials=creds)

        # Specify the task list and the date (e.g., '2023-12-31') for the task
        tasklist_id = ""


        # List all task lists
        task_lists = service.tasklists().list().execute()

        # Print the list of task lists along with their IDs
        for task_list in task_lists.get('items', []):
            if task_list['title'] == 'Chores':
                tasklist_id = task_list["id"]




        task_date = str(date.year) + '-' + str(date.month) + '-' + str(date.day)  # Replace with the desired date

        # Create a task
        task = {
            'title': task,
            'due': task_date + 'T00:00:00.000Z',  # Use midnight for the due date
        }

        created_task = service.tasks().insert(tasklist=tasklist_id, body=task).execute()

        print(f'Created task: {created_task["title"]}')
    except HttpError as err:
        print(err)


if __name__ == '__main__':
    main()
