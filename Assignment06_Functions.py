# ------------------------------------------------------------------------ #
# Title: Assignment 06
# Description: Working with functions in a class,
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# Fernando Hernandez, 11/17/2019, Modified code to complete assignment 6
#               by adding functions (processing and IO's)
# ------------------------------------------------------------------------ #

# Data -------------------------------------------------------------------- #
# Declare variables and constants
strFileName = "ToDoFile.txt"  # The name of the data file
objFile = None   # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}  # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A dictionary that acts as a 'table' of rows
strChoice = ""  # Capture the user option selection
strTask = "" # Capture the user Task
strPriority = "" # Capture the user Task Priority
strKeyToRemove = "" # Capture user Task to Remove from list
# Data -------------------------------------------------------------------- #


# Processing  ------------------------------------------------------------- #
class FileProcessor:
    """ Processing the data to and from a text file """

    @staticmethod
    def ReadFileDataToList(file_name, list_of_rows):
        # Desc - Reads data from a file into a list of dictionary rows

        file = open(file_name, "r")
        for line in file:
            data = line.split(",")
            row = {"Task": data[0].strip(), "Priority": data[1].strip()}
            list_of_rows.append(row)
        file.close()
        return list_of_rows

    @staticmethod
    def WriteListDataToFile(file_name, list_of_rows):
        # Desc - Write each row of data to the file

        objFile = open(file_name, "w")
        for dicRow in list_of_rows:
            objFile.write(dicRow["Task"] + "," + dicRow["Priority"] + "\n")
        objFile.close()

    @staticmethod
    def AddRowToList(task, priority, list_of_rows):
        # Create a new dictionary row
        dicRow = {"Task": task, "Priority": priority}
        list_of_rows.append(dicRow)  # Add the new row to the list/table

    @staticmethod
    def SearchTable(list_of_rows, key_to_remove):
        # Desc - Search though the table or rows for a match to the user's input
        intRowNumber = 0  # Create a counter to identify the current dictionary row in the loop

        while (intRowNumber < len(list_of_rows)):
            if (key_to_remove == str(list(dict(list_of_rows[intRowNumber]).values())[0])):  # Search current row column 0
                del list_of_rows[intRowNumber]  # Delete the row if a match is found
                blnItemRemoved = True  # Set the flag so the loop stops
            intRowNumber += 1  # Increase counter to get next row

# Processing  ------------------------------------------------------------- #

# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    """ A class for perform Input and Output """

    @staticmethod
    def OutputMenuItems():
        # Desc - Display a menu of choices to the user; returns (nothing)

        print('''
        Menu of Options
        1) Show current data
        2) Add a new item.
        3) Remove an existing item.
        4) Save Data to File
        5) Reload Data from File
        6) Exit Program
        ''')
        print()  # Add an extra line for looks

    @staticmethod
    def InputMenuChoice():
        # Desc - Gets the menu choice from a user; returns (string)

        choice = str(input("Which option would you like to perform? [1 to 6] - ")).strip()
        print()  # Add an extra line for looks
        return choice

    @staticmethod
    def ShowCurrentItemsInList(list_of_rows):
        # Desc - Shows the current items in the list of dictionaries rows; returns (nothing)

        print("******* The current items ToDo are: *******")
        for row in list_of_rows:
            print(row["Task"] + " (" + row["Priority"] + ")")
        print("*******************************************")
        print()  # Add an extra line for looks

    @staticmethod
    def Input_Task():
        # Desc - Accepts User Task Input; returns (task)

        task = str(input("What is the task? - ")).strip()
        print()
        return (task)

    @staticmethod
    def Input_Priority():
        # Desc - Accepts User Task Priority; returns (priority)

        priority = str(input("What is the priority? [high|low] - ")).strip()
        print()
        return (priority)


# Presentation (Input/Output)  -------------------------------------------- #

# Main Body of Script  ---------------------------------------------------- #

FileProcessor.ReadFileDataToList(strFileName, lstTable)  # read file data

while(True):
    IO.OutputMenuItems()  # Shows menu
    strChoice = IO.InputMenuChoice()  # Get menu option

    if (strChoice.strip() == '1'):
        IO.ShowCurrentItemsInList(lstTable)  # Show current data in the list/table
        continue  # to show the menu

    elif(strChoice.strip() == '2'):
        strTask = IO.Input_Task()
        strPriority = IO.Input_Priority()

        FileProcessor.AddRowToList(strTask, strPriority, lstTable)

        IO.ShowCurrentItemsInList(lstTable)  # Show current data in the list/table
        continue  # to show the menu

    elif(strChoice == '3'):

        strKeyToRemove = input("Which TASK would you like removed? - ")  # get task user wants deleted
        blnItemRemoved = False  # Create a boolean Flag for loop

        FileProcessor.SearchTable(lstTable, strKeyToRemove)

        if(blnItemRemoved == True):
            print("The task was removed.")
        else:
            print("I'm sorry, but I could not find that task.")
        print()  # Add an extra line for looks

        IO.ShowCurrentItemsInList(lstTable)  # Show current data in the list/table
        continue  # to show the menu

    elif(strChoice == '4'):

        IO.ShowCurrentItemsInList(lstTable)  # Show current data in the list/table

        if("y" == str(input("Save this data to file? (y/n) - ")).strip().lower()):  # Double-check with user

            FileProcessor.WriteListDataToFile(strFileName, lstTable)
            input("Data saved to file! Press the [Enter] key to return to menu.")
        else:
            input("New data was NOT Saved, but previous data still exists! Press the [Enter] key to return to menu.")
        continue

    elif (strChoice == '5'):
        print("Warning: This will replace all unsaved changes. Data loss may occur!")  # Warn user of data loss
        strYesOrNo = input("Reload file data without saving? [y/n] - ")  # Double-check with user
        if (strYesOrNo.lower() == 'y'):
            lstTable.clear()  # Added to fix bug 1.1.2030
            FileProcessor.ReadFileDataToList(strFileName, lstTable)  # Replace the current list data with file data
            IO.ShowCurrentItemsInList(lstTable)  # Show current data in the list/table
        else:
            input("File data was NOT reloaded! Press the [Enter] key to return to menu.")
            IO.ShowCurrentItemsInList(lstTable)  # Show current data in the list/table
        continue  # to show the menu

    elif (strChoice == '6'):
        break   # and Exit

# Main Body of Script  ---------------------------------------------------- #