import termcolor

termcolor.cprint("\nWelcome to To-do list application!\n", "light_blue")

todo_list = []

try:
    todo_list_file = open("list.txt", "r")
    todo_list = [line.strip() for line in todo_list_file.readlines()]
    todo_list_file.close()
except:
    pass

def menu():
    termcolor.cprint("Menu:\n", "yellow", attrs=["bold"])
    termcolor.cprint("1. Add an item to the list", "yellow", attrs=["bold"])
    termcolor.cprint("2. Remove an item from the list", "yellow", attrs=["bold"])
    termcolor.cprint("3. Mark an item as done", "yellow", attrs=["bold"])
    termcolor.cprint("4. View the list", "yellow", attrs=["bold"])
    termcolor.cprint("5. Exit", "yellow", attrs=["bold"])

menu()

while True:
    user_choice = input("\nEnter your choice: ")
    if user_choice == '1':
        item = input("\nEnter the item to add it to the list: ")
        if item in todo_list:
            termcolor.cprint("Item already exists in the list!", "red")
        else:
            todo_list.append(item)
            termcolor.cprint(f"Added item: {item} successfully", "green")

    elif user_choice == '2':
        item = input("\nEnter the item to remove from the list: ")
        if item in todo_list:
            todo_list.remove(item)
            termcolor.cprint(f"Item {item} removed successfully.", "green")
        else:
            termcolor.cprint("The item is not in the list!", "red")

    elif user_choice == '3':
        item = input("\nEnter the item to mark as done: ")
        if item in todo_list:
            todo_list.remove(item)
            termcolor.cprint(f"Item {item} is done! Removing from the list...", "green")
        else:
            termcolor.cprint("The item is not in the list!", "red")

    elif user_choice == '4':
        if todo_list == []:
            termcolor.cprint("The list is empty!", "yellow")
        else:
            print("\nItems:\n")
            for item in range(len(todo_list)):
                print(f"{item+1}. {todo_list[item]}")

    elif user_choice == '5':
        termcolor.cprint("\nClosing the application...\n", "light_blue")
        break
        
    else:
        termcolor.cprint("That is not a valid choice! Try again.\n", "red")
        menu()

todo_list_file = open("list.txt", "w")

if todo_list != []:
    for item in todo_list:
        todo_list_file.write(item+'\n')

todo_list_file.close()