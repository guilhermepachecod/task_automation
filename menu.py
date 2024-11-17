# menu.py

from user.menu import user_management_menu
from log.menu import log_management_menu  # Assuming you have a function to manage logs
from backup.menu import backup_menu  # Assuming you have a function for backup
from hardware.menu import hardware_menu  # Assuming you have a function to check hardware
from siem.menu import siem_menu  # Importing the SIEM menu
from network.menu import network_management_menu  # Importing the network management menu
from utils import clear_screen 

def show_menu():
    """Display the main menu and handle user choices."""
    while True:
        clear_screen()
        print("Menu:")
        print("1. Manage Users")
        print("2. Manage Logs")
        print("3. Manage Backup")
        print("4. Check Hardware")
        print("5. Manage Security")
        print("6. Manage Network")  # New option for network management
        print("0. Exit")

        choice = input("Choose an option: ")
        if handle_choice(choice):
            break

def handle_choice(choice):
    """Handle the user's menu choice."""
    if choice == '1':
        user_management_menu()
    elif choice == '2':
        log_management_menu()
    elif choice == '3':
        backup_menu()
    elif choice == '4':
        hardware_menu()
    elif choice == '5':
        siem_menu()  # Calling the SIEM menu to analyze security logs
    elif choice == '6':
        network_management_menu()  # Calling the network management menu
    elif choice == '0':
        print("Exiting...")
        return True 
    else:
        print("Invalid option. Please try again.")

    return False 
