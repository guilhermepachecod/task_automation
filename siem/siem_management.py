# siem/siem_management.py

import subprocess
import requests
import json
import platform
import time

def run_antivirus():
    """Run the antivirus and display the results."""
    try:
        # Example command to run an antivirus (replace with your antivirus)
        result = subprocess.run(['clamscan', '-r', '/'], capture_output=True, text=True)
        print("Antivirus Scan Results:")
        print(result.stdout)
    except Exception as e:
        print(f"An error occurred while running the antivirus: {e}")

def check_installed_packages():
    """Check and display installed packages."""
    try:
        # Check installed packages (example for Debian/Ubuntu systems)
        packages = subprocess.run(['dpkg', '--get-selections'], capture_output=True, text=True)
        print("Installed Packages:")
        print(packages.stdout)
    except Exception as e:
        print(f"An error occurred while checking installed packages: {e}")

def get_installed_applications():
    """Get a list of installed applications based on the operating system."""
    os_type = platform.system()
    
    if os_type == "Windows":
        return get_installed_applications_windows()
    elif os_type == "Linux":
        return get_installed_applications_linux()
    elif os_type == "Darwin":  # macOS
        return get_installed_applications_macos()
    else:
        print("Unsupported operating system.")
        return {}

def get_installed_applications_windows():
    """Get a list of installed applications on Windows using PowerShell."""
    try:
        output = subprocess.check_output(['powershell', '-Command', 'Get-WmiObject -Class Win32_Product | Select-Object -Property Name, Version | ConvertTo-Json'], universal_newlines=True)
        applications = json.loads(output)
        app_dict = {app['Name']: app['Version'] for app in applications}
        return app_dict
    except Exception as e:
        print(f"Error retrieving installed applications on Windows: {e}")
        return {}

def get_installed_applications_linux():
    """Get a list of installed applications on Linux using dpkg."""
    try:
        output = subprocess.check_output(['dpkg', '--get-selections'], universal_newlines=True)
        applications = {}
        
        # Split the output into lines
        for line in output.strip().split('\n'):
            if line and not line.startswith('deinstall'):
                parts = line.split('\t')  # Split by tab character
                name = parts[0]  # The first part is the package name
                # Get the package version
                try:
                    version = subprocess.check_output(['dpkg-query', '-W', '-f=${Version}', name], universal_newlines=True).strip()
                    applications[name] = version
                except subprocess.CalledProcessError:
                    applications[name] = "Version not found"
        
        return applications
    except Exception as e:
        print(f"Error retrieving installed applications on Linux: {e}")
        return {}

def get_installed_applications_macos():
    """Get a list of installed applications on macOS using Homebrew."""
    try:
        output = subprocess.check_output(['brew', 'list', '--versions'], universal_newlines=True)
        applications = {}
        
        # Split the output into lines
        for line in output.strip().split('\n'):
            if line:
                parts = line.split(' ')  # Split by spaces
                name = parts[0]  # The first part is the application name
                version = ' '.join(parts[1:])  # The rest are the versions (in case there are multiple)
                applications[name] = version
        
        return applications
    except Exception as e:
        print(f"Error retrieving installed applications on macOS: {e}")
        return {}

        
def check_cve_vulnerabilities():
    """Check for CVE vulnerabilities in installed applications."""
    try:
        # Get the list of installed applications
        installed_applications = get_installed_applications()
        
        # Dictionary to store found CVEs
        cve_results = {}

        # Check CVEs for each application
        for app_name, app_version in installed_applications.items():
            print(f"Checking CVEs for: {app_name} (version: {app_version})")
            response = requests.get(f'https://services.nvd.nist.gov/rest/json/cves/2.0?keywordSearch={app_name} {app_version}')

            # Check if the response was successful
            if response.status_code == 200:
                try:
                    cve_data = response.json()
                    if cve_data and 'result' in cve_data and 'CVE_Items' in cve_data['result']:
                        cve_results[app_name] = cve_data['result']['CVE_Items']
                except ValueError:
                    print(f"Error decoding JSON for package {app_name}. Response: {response.text}")
            else:
                print(f"Error accessing the API for package {app_name}. Status: {response.status_code}")

            # Delay of 2 seconds between requests
            time.sleep(5)

        # Print results
        # Print results
        total_found = sum(len(cves) for cves in cve_results.values())
        print(f"\nTotal CVEs found: {total_found}")

        if total_found > 0:
            show_details = input("Would you like to print the details of the found CVEs? (y/n): ")
            if show_details.lower() == 'y':
                for app_name, cves in cve_results.items():
                    print(f"\nCVEs for {app_name}:")
                    for cve in cves:
                        print(f"CVE: {cve['cve']['id']} - {cve['cve']['description']['description_data'][0]['value']}")
            else:
                print("Details will not be displayed.")
        else:
            print("No CVEs found for the installed applications.")

    except Exception as e:
        print(f"An error occurred while checking CVEs: {e}")

def check_firewall_status():
    """Check and display the current status of the firewall."""
    try:
        firewall_status = subprocess.run(['ufw', 'status'], capture_output=True, text=True)
        print("Firewall Status:")
        print(firewall_status.stdout)
    except Exception as e:
        print(f"An error occurred while checking the firewall status: {e}")

def check_system_logs_for_security():
    """Check and display the last 20 authentication logs for security."""
    try:
        with open('/var/log/auth.log', 'r') as file:
            logs = file.readlines()
            print("Last 20 Authentication Logs:")
            for line in logs[-20:]:
                print(line.strip())
    except Exception as e:
        print(f"An error occurred while checking security logs: {e}")
