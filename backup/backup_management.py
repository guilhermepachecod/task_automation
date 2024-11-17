# backup/backup_management.py

import os
import shutil
from datetime import datetime

BACKUP_DIR = 'DATA/backup/'  # Change to the desired backup directory

def backup_user_files():
    """Backup user files to the specified backup directory."""
    try:
        user_files_dir = '/etc/'  # Change to the user files directory
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        backup_path = os.path.join(BACKUP_DIR, f'backup_{timestamp}')
        
        shutil.copytree(user_files_dir, backup_path)
        print(f"Backup successfully created at: {backup_path}")
    except PermissionError:
        print("Permission error: You do not have access to this directory.")
    except Exception as e:
        print(f"An error occurred while backing up files: {e}")

def view_backup_history():
    """View the history of backups."""
    try:
        backups = os.listdir(BACKUP_DIR)
        if backups:
            print("Backup History:")
            for backup in backups:
                print(backup)
        else:
            print("No backups found.")
    except PermissionError:
        print("Permission error: You do not have access to this directory.")
    except Exception as e:
        print(f"An error occurred while viewing the backup history: {e}")

def restore_backup():
    """Restore a backup from the specified backup directory."""
    try:
        backup_to_restore = input("Enter the name of the backup you want to restore: ")
        backup_path = os.path.join(BACKUP_DIR, backup_to_restore)
        
        if os.path.exists(backup_path):
            user_files_dir = '/path/to/user/files'  # Change to the user files directory
            shutil.rmtree(user_files_dir)  # Remove current files
            shutil.copytree(backup_path, user_files_dir)  # Restore the backup
            print(f"Backup successfully restored from: {backup_path}")
        else:
            print("Backup not found.")
    except PermissionError:
        print("Permission error: You do not have access to this directory.")
    except Exception as e:
        print(f"An error occurred while restoring the backup: {e}")

def delete_backup():
    """Delete a specified backup from the backup directory."""
    try:
        backup_to_delete = input("Enter the name of the backup you want to delete: ")
        backup_path = os.path.join(BACKUP_DIR, backup_to_delete)
        
        if os.path.exists(backup_path):
            shutil.rmtree(backup_path)
            print(f"Backup successfully deleted: {backup_path}")
        else:
            print("Backup not found.")
    except PermissionError:
        print("Permission error: You do not have access to this directory.")
    except Exception as e:
        print(f"An error occurred while deleting the backup: {e}")

# Example usage of the functions
if __name__ == "__main__":
    backup_user_files()
    view_backup_history()
    restore_backup()
    delete_backup()
