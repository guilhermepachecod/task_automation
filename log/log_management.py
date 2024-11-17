# log/log_management.py

import os
import time

def view_security_logs():
    """View and display the last 10 security logs."""
    try:
        with open('/var/log/auth.log', 'r') as f:  # Example of security log
            logs = f.readlines()
            for log in logs[-10:]:  # Display the last 10 lines
                print(log.strip())
    except PermissionError:
        print("Permission error: You do not have access to this file.")
    except Exception as e:
        print(f"An error occurred while viewing security logs: {e}")

def view_error_logs():
    """View and display the last 10 error logs."""
    try:
        with open('/var/log/syslog', 'r') as f:  # Example of error log
            logs = f.readlines()
            for log in logs[-10:]:  # Display the last 10 lines
                print(log.strip())
    except PermissionError:
        print("Permission error: You do not have access to this file.")
    except Exception as e:
        print(f"An error occurred while viewing error logs: {e}")

def view_intrusion_attempts():
    """View and display intrusion attempts from the logs."""
    try:
        with open('/var/log/auth.log', 'r') as f:  # Example of intrusion attempts log
            logs = f.readlines()
            for log in logs:
                if "Failed password" in log:  # Filter intrusion attempts
                    print(log.strip())
    except PermissionError:
        print("Permission error: You do not have access to this file.")
    except Exception as e:
        print(f"An error occurred while viewing intrusion attempts logs: {e}")

def view_firewall_logs():
    """View and display the last 10 firewall logs."""
    try:
        with open('/var/log/ufw.log', 'r') as f:  # Example of firewall log
            logs = f.readlines()
            for log in logs[-10:]:  # Display the last 10 lines
                print(log.strip())
    except PermissionError:
        print("Permission error: You do not have access to this file.")
    except Exception as e:
        print(f"An error occurred while viewing firewall logs: {e}")

def list_all_firewall_logs():
    """List and display all firewall logs."""
    try:
        with open('/var/log/ufw.log', 'r') as f:
            logs = f.readlines()
            for log in logs:  # Display all lines
                print(log.strip())
    except PermissionError:
        print("Permission error: You do not have access to this file.")
    except Exception as e:
        print(f"An error occurred while listing all firewall logs: {e}")

def monitor_firewall_logs():
    """Monitor firewall logs in real-time."""
    try:
        with open('/var/log/ufw.log', 'r') as f:
            # Move the pointer to the end of the file
            f.seek(0, os.SEEK_END)
            while True:
                line = f.readline()
                if not line:
                    time.sleep(0.5)  # Wait for new log entries
                    continue
                print(line.strip())
    except PermissionError:
        print("Permission error: You do not have access to this file.")
    except Exception as e:
        print(f"An error occurred while monitoring firewall logs: {e}")

def view_login_history():
    """View and display login history."""
    try:
        with open('/var/log/auth.log', 'r') as f:  # Example of login history
            logs = f.readlines()
            for log in logs:
                if "session opened" in log or "session closed" in log:  # Filter login sessions
                    print(log.strip())
    except PermissionError:
        print("Permission error: You do not have access to this file.")
    except Exception as e:
        print(f"An error occurred while viewing login history: {e}")

def view_command_history():
    """View and display command history."""
    try:
        with open(os.path.expanduser('~/.bash_history'), 'r') as f:  # Adjust the path as necessary
            logs = f.readlines()
            for log in logs:
                print(log.strip())
    except FileNotFoundError:
        print("Command history file not found.")
    except PermissionError:
        print("Permission error: You do not have access to this file.")
    except Exception as e:
        print(f"An error occurred while viewing command history: {e}")

# Example of using the functions
if __name__ == "__main__":
    view_security_logs()
    view_error_logs()
    view_intrusion_attempts()
    view_firewall_logs()
