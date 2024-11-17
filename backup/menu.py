# backup/backup_management.py

from backup.backup_management import (
    backup_user_files,
    view_backup_history,
    restore_backup,
    delete_backup
)
from utils import (clear_screen, pause)

def backup_menu():
    """Display the backup management menu and handle user choices."""
    clear_screen()
    while True:
        print("\nBackup Management:")
        print("1. Backup User Files")
        print("2. View Backup History")
        print("3. Restore Backup")
        print("4. Delete Backup")
        print("0. Return to Main Menu")

        choice = input("Choose an option: ")
        if handle_backup_choice(choice):
            break

def handle_backup_choice(choice):
    """Handle the user's backup menu choice."""
    if choice == '1':
        backup_user_files()
    elif choice == '2':
        view_backup_history()
    elif choice == '3':
        restore_backup()
    elif choice == '4':
        delete_backup()
    elif choice == '0':
        return True
    else:
        print("Invalid option. Please try again.")
    
    pause()
    return False
