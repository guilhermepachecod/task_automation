# siem/menu.py

from siem.siem_management import (
    run_antivirus,
    check_installed_packages,
    check_cve_vulnerabilities,
    check_firewall_status,
    check_system_logs_for_security
)
from utils import (clear_screen, pause)

def siem_menu():
    """Display the SIEM security check menu and handle user choices."""
    while True:
        clear_screen()
        print("\nSecurity Check (SIEM):")
        print("1. Run Antivirus")
        print("2. Check Installed Packages")
        print("3. Check CVE Vulnerabilities")
        print("4. Check Firewall Status")
        print("5. Check Security Logs")
        print("0. Return to Main Menu")

        choice = input("Choose an option: ")
        if handle_siem_choice(choice):
            break

def handle_siem_choice(choice):
    """Handle the user's SIEM menu choice."""
    if choice == '1':
        run_antivirus()
    elif choice == '2':
        check_installed_packages()
    elif choice == '3':
        check_cve_vulnerabilities()
    elif choice == '4':
        check_firewall_status()
    elif choice == '5':
        check_system_logs_for_security()
    elif choice == '0':
        return True
    else:
        print("Invalid option. Please try again.")
    
    pause()
    return False
