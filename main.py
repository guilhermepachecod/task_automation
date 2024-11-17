# task_automation/main.py

import os
from menu import show_menu

def check_sudo():
    """Check if the script is being run with superuser privileges."""
    if os.geteuid() != 0:  # Check if the user ID is not 0
        print("This program must be run with superuser privileges (sudo).")
        exit(1)  # Exit the program with exit code 1

def main():
    """Main function to run the task automation system."""
    check_sudo()  # Check if running as sudo
    print("Welcome to the Task Automation System!")
    show_menu()

if __name__ == "__main__":
    main()
