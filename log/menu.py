# log/menu.py

from log.log_management import (
    view_security_logs,
    view_error_logs,
    view_intrusion_attempts,
    view_firewall_logs,
    list_all_firewall_logs,
    monitor_firewall_logs,
    view_login_history,
    view_command_history
)
from utils import (clear_screen, pause)

def log_management_menu():
    """Display the log management menu and handle user choices."""
    while True:
        clear_screen()
        print("\nLog Management:")
        print("1. View Security Logs")
        print("2. View Error Logs")
        print("3. View Intrusion Attempts")
        print("4. View Firewall Logs")
        print("5. List All Firewall Logs")
        print("6. Monitor Firewall Logs Live")
        print("7. View Login History")
        print("8. View Command History")
        print("0. Return to Main Menu")

        choice = input("Choose an option: ")
        if handle_log_management_choice(choice):
            break

def handle_log_management_choice(choice):
    """Handle the user's log management menu choice."""
    if choice == '1':
        view_security_logs()
    elif choice == '2':
        view_error_logs()
    elif choice == '3':
        view_intrusion_attempts()
    elif choice == '4':
        view_firewall_logs()
    elif choice == '5':
        list_all_firewall_logs()
    elif choice == '6':
        print("Starting to monitor firewall logs (press Ctrl+C to stop)...")
        monitor_firewall_logs()
    elif choice == '7':
        view_login_history()
    elif choice == '8':
        view_command_history()
    elif choice == '0':
        return True
    else:
        print("Invalid option. Please try again.")
    
    pause()
    return False
