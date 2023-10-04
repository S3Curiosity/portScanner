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

## License

This project is licensed under the MIT License.
```
https://twitter.com/S3Curiosity
