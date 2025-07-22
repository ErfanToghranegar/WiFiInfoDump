# WiFiInfoDump
A Python script that extracts and displays saved Wi-Fi network information on Windows systems, including:  Network Name (SSID)  Password  Authentication Method  Encryption Type.

## Features

- Lists all saved Wi-Fi profiles on the system.
- Retrieves password and security details for each profile.
- Outputs the information in a clear and readable format.

## Requirements

- Windows operating system.
- Python 3.x installed.
- Run the script with administrator privileges to access Wi-Fi passwords.

## Usage

1. Clone this repository or download the `wifi_secrets.py` script.
2. Open a command prompt with **administrator rights**.
3. Navigate to the directory containing the script.
4. Run the script using:

```bash
python wifi_secrets.py

How It Works
The script uses Windows' built-in netsh command to list Wi-Fi profiles and then retrieves detailed information for each profile, including the saved password if available. It uses Python's subprocess module to run system commands and re module to parse the output.

Disclaimer
This script is designed for educational purposes.

Use it responsibly and only on networks you have permission to access.

Passwords and sensitive information are retrieved locally and not sent anywhere.
