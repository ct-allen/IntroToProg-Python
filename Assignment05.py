# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# CAllen,5.11.2023,Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFile = "ToDoList.txt"   # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated1 into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = "" # A Capture the user option selection


# -- Processing -- #
# Step 1 - When the program starts, load any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)

try:
    objFile = open('ToDoList.txt', 'r')
    for row in objFile:
        lstrow = row.split(',')
        dicRow = {"Task": lstrow[0], "Priority": lstrow[1].strip()}
        print(dicRow['Task'] + '|' + dicRow['Priority'].strip())
        lstTable.append(dicRow)
    objFile.close()
except:
    print('File not found, will make a new file when you save')


# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show Current Data
    2) Add a New Item
    3) Remove an Existing Item
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks
    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        for objRow in lstTable:
            print(objRow)

    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        useritem = input('Enter an Task:')
        uservalue = input('Enter a Priority:')
        dicRow = {'Task': useritem, 'Priority': uservalue}
        lstTable.append(dicRow)
        continue

    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):
        strItem = input("Item to Remove: ")
        for row in lstTable:
            if row["Task"].lower() == strItem.lower():
                lstTable.remove(row)
                print("Row Removed")
            else:
                print("Row Not Found")
        continue

    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif (strChoice.strip() == '4'):
        objFile = open('ToDoList.txt', "w")
        for dicRow in lstTable:
            objFile.write(dicRow['Task'] + "," + dicRow['Priority'] + "\n")
        objFile.close()
        print('Saved!')
        continue

    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        print('Goodbye!')
        break  # and Exit the program
    else:
        print('Please pick an option 1 thru 5')
