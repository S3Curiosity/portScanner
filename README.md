# Port Scanning Script

This Python script allows you to perform port scanning on one or multiple targets to check if specific ports are open.

## Features

- Scans one or multiple targets for open ports.
- Supports custom port range.
- Concurrent port scanning for faster results.
- Handles socket timeouts gracefully.

## Prerequisites

- Python 3.x

## Usage

1. Clone this repository or download the script.
2. Open your terminal/command prompt.
3. Navigate to the directory where the script is located.

### Running the Script

To run the script, use the following command:

```bash
python port_scanner.py
```

You will be prompted to enter the targets and the number of ports you want to scan.

- Enter the targets separated by commas (e.g., `192.168.1.1, 192.168.1.2`).
- Specify the number of ports you want to scan.

The script will start scanning the specified ports on the provided targets and display the results.

## Example

```bash
[*] Enter Targets To Scan (split them by ,): 192.168.1.1
[*] Enter How Many Ports You Want To Scan: 100
Starting Scan For 192.168.1.1
[+] Port 22 Opened
[+] Port 80 Opened
...
```
## Disclaimer

This is for educational purposes only. 
Always ensure you have proper authorization before conducting any security testing on systems or networks you do not own or have explicit permission to test.
Please use this script responsibly and ensure that you have the right to test the target in question.

The authors and contributors of this script are not responsible for any misuse or legal consequences that may arise from its use.

## License

This script is open-source software licensed under the [MIT License] Feel free to use, modify, and distribute it as per the terms of the license.

---

## License

This project is licensed under the MIT License.
```
https://twitter.com/S3Curiosity
