# task_automation/user/menu.py

from user.user_management import (
    add_user,
    remove_user,
    list_users,
    change_password,
    list_groups,
    add_group,
    remove_group
)
from utils import (clear_screen, pause)

def user_management_menu():
    """Display the user management menu and handle user choices."""
    while True:
        clear_screen()
        print("\nUser Management:")
        print("1. Add User")
        print("2. Remove User")
        print("3. List Users")
        print("4. Change User Password")
        print("5. List Groups")
        print("6. Add Group")
        print("7. Remove Group")
        print("0. Return to Main Menu")

        choice = input("Choose an option: ")
        if handle_user_management_choice(choice):
            break

def handle_user_management_choice(choice):
    """Handle the user's management menu choice."""
    if choice == '1':
        username = input("Enter the username to be added: ")
        add_user(username)
    elif choice == '2':
        username = input("Enter the username to be removed: ")
        remove_user(username)
    elif choice == '3':
        list_users()
    elif choice == '4':
        username = input("Enter the username whose password will be changed: ")
        new_password = input("Enter the new password: ")
        change_password(username, new_password)
    elif choice == '5':
        list_groups()
    elif choice == '6':
        groupname = input("Enter the group name to be added: ")
        add_group(groupname)
    elif choice == '7':
        groupname = input("Enter the group name to be removed: ")
        remove_group(groupname)
    elif choice == '0':
        return True
    else:
        print("Invalid option. Please try again.")
    
    pause()
    return False
