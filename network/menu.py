# network/menu.py

from network.network_management import (
    view_network_connections,
    view_active_sessions,
    view_network_statistics,
    view_firewall_status,
    monitor_network_traffic,
    # Add additional functions here as they are implemented
)
from utils import (clear_screen, pause)

def network_management_menu():
    """Display the network management menu and handle user choices."""
    while True:
        clear_screen()
        print("\nNetwork Management:")
        print("1. View Network Connections")
        print("2. View Active Sessions")
        print("3. View Network Statistics")
        print("4. View Firewall Status")
        print("5. Monitor Network Traffic")
        print("0. Return to Main Menu")

        choice = input("Choose an option: ")
        if handle_network_management_choice(choice):
            break

def handle_network_management_choice(choice):
    """Handle the user's network management menu choice."""
    if choice == '1':
        view_network_connections()
    elif choice == '2':
        view_active_sessions()
    elif choice == '3':
        view_network_statistics()
    elif choice == '4':
        view_firewall_status()
    elif choice == '5':
        monitor_network_traffic()
    elif choice == '0':
        return True
    else:
        print("Invalid option. Please try again.")
    
    pause()
    return False
