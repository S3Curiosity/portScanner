import socket
import termcolor
import concurrent.futures

def scan_port(ipaddress, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(1)  # Set a timeout for socket connection
            result = sock.connect_ex((ipaddress, port))
            if result == 0:
                print(termcolor.colored(f"[+] Port {port} Opened", 'green'))
    except Exception as e:
        pass

def scan(target, ports):
    print('\n' + 'Starting Scan For ' + str(target))
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(scan_port, target, port) for port in range(1, ports)]
        concurrent.futures.wait(futures)

if __name__ == "__main__":
    targets = input("[*] Enter Targets To Scan (split them by ,): ")
    ports = int(input("[*] Enter How Many Ports You Want To Scan: "))

    if ',' in targets:
        print(termcolor.colored("[*] Scanning Multiple Targets", 'green'))
        for ip_addr in targets.split(','):
            scan(ip_addr.strip(), ports)
    else:
        scan(targets, ports)
