macOS Resource Monitor
A lightweight, real-time resource monitor for macOS using Python and tkinter.

Description
This utility provides a real-time overview of key system metrics including CPU, RAM, and storage usage. With its minimalistic and unobtrusive interface, it can be easily positioned anywhere on the screen, giving you a quick glance into your system's performance.

Installation
Clone the repository:

bash
Copy code
git clone https://github.com/zac-bostick/macos-resource-monitor.git
Navigate to the project directory:

bash
Copy code
cd macos-resource-monitor
Install the required packages:

bash
Copy code
pip install -r requirements.txt
Usage
Run the script:

bash
Copy code
python3 monitor.py
Running at Startup:
Create a plist file named com.yourname.resourcemonitor.plist in ~/Library/LaunchAgents/.

Add the following content to the plist file:

xml
Copy code
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.yourname.resourcemonitor</string>
    
    <key>Program</key>
    <string>/usr/local/bin/python3 /path/to/your/resources.py</string>
    
    <key>RunAtLoad</key>
    <true/>
    
    <key>KeepAlive</key>
    <false/>
</dict>
</plist>
Load the plist file:

bash
Copy code
launchctl load ~/Library/LaunchAgents/com.yourname.resourcemonitor.plist
Reboot to test.

Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

License
MIT

