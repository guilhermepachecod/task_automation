# task_automation/utils.py

import os

def print_message(message):
    """Print an informational message."""
    print(f"[INFO] {message}")

def log_error(error_message):
    """Log an error message."""
    print(f"[ERROR] {error_message}")

def clear_screen():
    """Clear the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def pause():
    """Pause the execution and wait for user input."""
    input("Press Enter to continue...")
