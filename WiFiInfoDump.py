import subprocess
import re

def get_wifi_details():
    # Running the command to get the list of Wi-Fi profiles
    command = "netsh wlan show profiles"
    result = subprocess.run(command, capture_output=True, text=True, shell=True)

    wifi_profiles = {}

    # Regular expressions to match relevant information
    name_wifi = r"Profile\s*:\s*(.*)"
    get_password = r"Key Content\s*:\s*(.*)"
    security = r"Authentication\s*:\s*(.*)"
    encryption = r"Cipher\s*:\s*(.*)"

    
    ssid_matches = re.findall(name_wifi, result.stdout)

    for ssid in ssid_matches:
        command_details = f'netsh wlan show profile "{ssid}" key=clear'
        result_details = subprocess.run(command_details, capture_output=True, text=True, shell=True)

        
        password_match = re.search(get_password, result_details.stdout)
        password = password_match.group(1) if password_match else None

        security_match = re.search(security, result_details.stdout)
        authentication = security_match.group(1) if security_match else None

        encryption_match = re.search(encryption, result_details.stdout)
        cipher = encryption_match.group(1) if encryption_match else None

        # Store the details in a dictionary
        wifi_profiles[ssid] = {
            "Password": password,
            "Authentication": authentication,
            "Encryption": cipher
        }

    return wifi_profiles

# Main function to display the results
def main():
    wifi_profiles = get_wifi_details()
    
    if not wifi_profiles:
        print("No Wi-Fi profiles found.")
        return
    
    # Print the Wi-Fi profiles and their details
    for ssid, details in wifi_profiles.items():
        print(f"SSID: {ssid}")
        print(f"Password: {details['Password'] if details['Password'] else 'Not set or not found'}")
        print(f"Authentication: {details['Authentication'] if details['Authentication'] else 'Not found'}")
        print(f"Encryption: {details['Encryption'] if details['Encryption'] else 'Not found'}")
        print("-" * 40)

if __name__ == "__main__":
    main()
