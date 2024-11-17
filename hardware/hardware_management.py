# hardware/hardware_management.py

import psutil
import subprocess

def check_cpu_usage():
    """Check and display CPU usage."""
    try:
        cpu_usage = psutil.cpu_percent(interval=1)
        print(f"CPU Usage: {cpu_usage}%")
    except Exception as e:
        print(f"An error occurred while checking CPU usage: {e}")

def check_memory_usage():
    """Check and display memory usage."""
    try:
        memory = psutil.virtual_memory()
        print(f"Memory Usage: {memory.percent}%")
        print(f"Total Memory: {memory.total / (1024 ** 2):.2f} MB")
        print(f"Used Memory: {memory.used / (1024 ** 2):.2f} MB")
        print(f"Free Memory: {memory.available / (1024 ** 2):.2f} MB")
    except Exception as e:
        print(f"An error occurred while checking memory usage: {e}")

def check_disk_usage():
    """Check and display disk usage."""
    try:
        disk = psutil.disk_usage('/')
        print(f"Disk Usage: {disk.percent}%")
        print(f"Total Space: {disk.total / (1024 ** 3):.2f} GB")
        print(f"Used Space: {disk.used / (1024 ** 3):.2f} GB")
        print(f"Free Space: {disk.free / (1024 ** 3):.2f} GB")
    except Exception as e:
        print(f"An error occurred while checking disk usage: {e}")

def check_network_status():
    """Check and display the status of network interfaces."""
    try:
        network = psutil.net_if_stats()
        print("Network Status:")
        for interface, stats in network.items():
            status = "Up" if stats.isup else "Down"
            print(f"{interface}: {status} (Speed: {stats.speed} Mbps)")
    except Exception as e:
        print(f"An error occurred while checking network status: {e}")

def check_filesystem():
    """Check the filesystem for errors."""
    try:
        result = subprocess.run(['fsck', '-n', '/dev/sda1'], capture_output=True, text=True)
        print("Filesystem Check:")
        print(result.stdout)
    except Exception as e:
        print(f"An error occurred while checking the filesystem: {e}")

def repair_boot():
    """Attempt to repair the bootloader."""
    try:
        result = subprocess.run(['grub-install', '/dev/sda'], capture_output=True, text=True)
        print("Boot Repair:")
        print(result.stdout)
    except Exception as e:
        print(f"An error occurred while attempting to repair the boot: {e}")

def check_common_errors():
    """Check for common errors in system logs."""
    try:
        with open('/var/log/syslog', 'r') as file:
            logs = file.readlines()
            print("Common Errors Found in Log:")
            for line in logs[-20:]:
                if 'error' in line.lower():
                    print(line.strip())
    except Exception as e:
        print(f"An error occurred while checking for common errors: {e}")

def check_running_services():
    """Check and display running services."""
    try:
        services = subprocess.run(['systemctl', 'list-units', '--type=service'], capture_output=True, text=True)
        print("Running Services:")
        print(services.stdout)
    except Exception as e:
        print(f"An error occurred while checking running services: {e}")

def check_system_logs():
    """Display the last 20 system logs."""
    try:
        with open('/var/log/syslog', 'r') as file:
            logs = file.readlines()
            print("Last 20 System Logs:")
            for line in logs[-20:]:
                print(line.strip())
    except Exception as e:
        print(f"An error occurred while checking system logs: {e}")

def check_firewall_status():
    """Check and display the status of the firewall."""
    try:
        firewall_status = subprocess.run(['ufw', 'status'], capture_output=True, text=True)
        print("Firewall Status:")
        print(firewall_status.stdout)
    except Exception as e:
        print(f"An error occurred while checking the firewall status: {e}")

def check_os_version():
    """Check and display the operating system version."""
    try:
        os_version = subprocess.run(['lsb_release', '-a'], capture_output=True, text=True)
        print("Operating System Version:")
        print(os_version.stdout)
    except Exception as e:
        print(f"An error occurred while checking the operating system version: {e}")

def check_cpu_temperature():
    """Check and display the CPU temperature."""
    try:
        temp = subprocess.run(['sensors'], capture_output=True, text=True)
        print("CPU Temperature:")
        print(temp.stdout)
    except Exception as e:
        print(f"An error occurred while checking the CPU temperature: {e}")

def check_memory_usage_by_process():
    """Check and display memory usage by process."""
    try:
        memory_usage = subprocess.run(['ps', '-eo', 'pid,comm,%mem'], capture_output=True, text=True)
        print("Memory Usage by Process:")
        print(memory_usage.stdout)
    except Exception as e:
        print(f"An error occurred while checking memory usage by process: {e}")

def check_active_network_connections():
    """Check and display active network connections."""
    try:
        connections = subprocess.run(['ss', '-tuln'], capture_output=True, text=True)
        print("Active Network Connections:")
        print(connections.stdout)
    except Exception as e:
        print(f"An error occurred while checking active network connections: {e}")

def check_storage_devices():
    """Check and display storage devices."""
    try:
        devices = subprocess.run(['lsblk'], capture_output=True, text=True)
        print("Storage Devices:")
        print(devices.stdout)
    except Exception as e:
        print(f"An error occurred while checking storage devices: {e}")

# Main block to execute the functions
if __name__ == "__main__":
    check_cpu_usage()
    check_memory_usage()
    check_disk_usage()
    check_network_status()
    check_filesystem()  # Check the filesystem
    repair_boot()       # Attempt to repair the boot
    check_common_errors()  # Check for common errors
    check_running_services()  # Check running services
    check_system_logs()  # Check system logs
    check_firewall_status()  # Check firewall settings
    check_os_version()  # Check operating system version
    check_cpu_temperature()  # Check CPU temperature
    check_memory_usage_by_process()  # Check memory usage by process
    check_active_network_connections()  # Check active network connections
    check_storage_devices()  # Check storage devices
