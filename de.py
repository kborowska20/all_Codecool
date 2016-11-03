import sys

def deleteContent(fName):
    with open(fName, "w"):
        pass


def file_len():
    count = (len(listOfTasks) + 1)
    return count


listOfTasks = []
listOfMarkedItems = []
f = open("marked.list","r")
d = open("tasks.list","r")

for line in f:
    listOfMarkedItems.append(bool(line))


for line in d:
    if line not in listOfTasks:
        listOfTasks.append(line)

f.close()
d.close()
deleteContent("marked.list")
deleteContent("tasks.list")

def main():
    #Menu
    command = input("Please specify a command: [list, add, mark, archive,exit]: ")
    commands = ["list","add","mark","archive"]
    if command == "list":
        ListTask()
    elif command == "add":
        AddTask()
    elif command == "mark":
        print("You saved the following to-do items:")
        ListTask()
        choose = input("Which one you want to mark as completed: ")
        MarkAsComplete(choose)
    elif command == "archive":
        Archive()
    elif command == "exit":
        ExitProgram()



def ListTask():
    for i in range(0,len(listOfTasks)):
        print("{}. {}".format(i+1,listOfTasks[i]))


def AddTask():
    #adding a new task
    counter = file_len()
    tempItem = input("Add an item: ")
    listOfMarkedItems.append(False)
    listOfTasks.append("[{}] {}".format(listOfMarkedItems[counter-1], tempItem))
    print("Item added.")


def MarkAsComplete(number):
    number = int(number)
    tempString = listOfTasks[number - 1]
    tempString = tempString.replace("False","True")
    listOfTasks[number - 1] = tempString
    listOfMarkedItems[number-1] = True

def Archive():
    for i in range(len(listOfMarkedItems)-1):
        if(listOfMarkedItems[i-1] == True):
            del listOfMarkedItems[i-1]
            del listOfTasks[i-1]
    print("All completed tasks got deleted.")



def ExitProgram():
    f = open("marked.list","a")
    d = open("tasks.list","a")
    for i in range(0,len(listOfMarkedItems)):
        f.write(str(listOfMarkedItems[i])+"\n")
    for i in range(0,len(listOfTasks)):
        d.write(listOfTasks[i]+"\n")
    f.close()
    d.close()
    sys.exit(0)

while True:
    main()
