# macOS Resource Monitor

A lightweight, real-time resource monitor for macOS using Python and `tkinter`.

## Description

This utility provides a real-time overview of key system metrics including CPU, RAM, and storage usage. With its minimalistic and unobtrusive interface, it can be easily positioned anywhere on the screen, giving you a quick glance into your system's performance.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/zac-bostick/macos-resource-monitor.git
   ```

2. Navigate to the project directory:

   ```bash
   cd macos-resource-monitor
   ```

3. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the script:

   ```bash
   python3 resources.py
   ```

### Running at Startup:

1. Create a plist file named `com.yourname.resourcemonitor.plist` in `~/Library/LaunchAgents/`.

2. Add the following content to the plist file:

   ```xml
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
   ```

3. Load the plist file:

   ```bash
   launchctl load ~/Library/LaunchAgents/com.yourname.resourcemonitor.plist
   ```

4. Reboot to test.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://github.com/zac-bostick/macos-resource-monitor/blob/main/LICENSE)

---
