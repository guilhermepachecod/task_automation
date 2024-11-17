# hardware/menu.py

from hardware.hardware_management import (
    check_cpu_usage,
    check_memory_usage,
    check_disk_usage,
    check_network_status,
    check_filesystem,
    repair_boot,
    check_common_errors,
    check_running_services,
    check_system_logs,
    check_firewall_status,
    check_os_version,
    check_cpu_temperature,
    check_memory_usage_by_process,
    check_active_network_connections,
    check_storage_devices
)
from utils import (clear_screen, pause)

def hardware_menu():
    """Display the hardware check menu and handle user choices."""
    while True:
        clear_screen()
        print("\nHardware Check:")
        print("1. Check CPU Usage")
        print("2. Check Memory Usage")
        print("3. Check Disk Usage")
        print("4. Check Network Status")
        print("5. Check Filesystem")
        print("6. Repair Boot")
        print("7. Check Common Errors")
        print("8. Check Running Services")
        print("9. Check System Logs")
        print("10. Check Firewall Status")
        print("11. Check Operating System Version")
        print("12. Check CPU Temperature")
        print("13. Check Memory Usage by Process")
        print("14. Check Active Network Connections")
        print("15. Check Storage Devices")
        print("0. Return to Main Menu")

        choice = input("Choose an option: ")
        if handle_hardware_choice(choice):
            break

def handle_hardware_choice(choice):
    """Handle the user's hardware menu choice."""
    if choice == '1':
        check_cpu_usage()
    elif choice == '2':
        check_memory_usage()
    elif choice == '3':
        check_disk_usage()
    elif choice == '4':
        check_network_status()
    elif choice == '5':
        check_filesystem()
    elif choice == '6':
        repair_boot()
    elif choice == '7':
        check_common_errors()
    elif choice == '8':
        check_running_services()
    elif choice == '9':
        check_system_logs()
    elif choice == '10':
        check_firewall_status()
    elif choice == '11':
        check_os_version()
    elif choice == '12':
        check_cpu_temperature()
    elif choice == '13':
        check_memory_usage_by_process()
    elif choice == '14':
        check_active_network_connections()
    elif choice == '15':
        check_storage_devices()
    elif choice == '0':
        return True
    else:
        print("Invalid option. Please try again.")
    
    pause()
    return False
