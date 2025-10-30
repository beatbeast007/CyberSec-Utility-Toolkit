import subprocess
import re

def get_wifi_passwords():
    profiles = subprocess.check_output(
        "netsh wlan show profiles", shell=True
    ).decode(errors="ignore")
    wifi_names = re.findall("All User Profile     : (.*)", profiles)

    for name in wifi_names:
        results = subprocess.check_output(
            f"netsh wlan show profile name=\"{name}\" key=clear", shell=True
        ).decode(errors="ignore")
        password = re.search("Key Content            : (.*)", results)
        print(f"SSID: {name} | Password: {password.group(1) if password else 'N/A'}")

if __name__ == "__main__":
    get_wifi_passwords()
