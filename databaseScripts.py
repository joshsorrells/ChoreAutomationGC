
import sqlite3



def add_tables(conn):
    pass

def insert_into_chores(conn, name, effortPoints, lastCompleted, dateAssigned, lastCompletedBy, numDaysPerInterval, intervalInDays, highPriority, mustRotate, specificAssignee, room):
    # Create a cursor
    cursor = conn.cursor()
    cursor.execute("INSERT INTO chores (name, effortPoints, lastCompleted, dateAssigned, lastCompletedBy, numDaysPerInterval, intervalInDays, highPriority, mustRotate, specificAssignee, room) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", name, effortPoints, lastCompleted, dateAssigned, lastCompletedBy, numDaysPerInterval, intervalInDays, highPriority, mustRotate, specificAssignee, room)

def insert_into_chores_from_CSV(conn, filename):
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS chores (
        id INTEGER PRIMARY KEY,
        name TEXT,
        effortPoints INTEGER,
        lastCompleted DATE,
        dateAssigned DATE,
        lastCompletedBy TEXT,
        numDaysPerInterval INT,
        intervalInDays INT,
        highPriority INT,
        mustRotate INT,
        specificAssignee TEXT,
        room TEXT
    )
    ''')

def insertIntoUsers(conn, username, taskListName):
    #convert task list name to ID before storing
    pass

def insertIntoHistory(conn, choreID, completedBy, dateCompleted):
    pass

def insertIntoTaskLists(conn, name, taskListID):
    pass

def insertIntoCalendars(conn, calendarName, ownedBy):
    pass 



if __name__ == '__main__':

    #this script will create the database
    conn = sqlite3.connect('myDatabase.db')

    insert_into_chores_from_CSV(conn, "chores.csv")
    insertIntoUsers(conn, "Josh")
    insertIntoTaskLists(conn, "Josh", "Chores")
    insertIntoCalendars(conn, 'primary', "Josh")







    conn.commit()
    conn.close()