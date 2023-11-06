

from calendarScripts import *
from datetime import date
from taskScripts import *










if __name__ == '__main__':

    conn = sqlite3.connect('mydatabase.db')

    output = calendar_availability(period = 1)
    for key in output:
        print(key)
        if date.today() != key:
            print(f"Creating task on {date}")
            create_task_for_user(username="Josh", date = key, task= "Test")


    conn.commit()
    conn.close()