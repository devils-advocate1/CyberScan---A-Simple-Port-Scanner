import socket
from datetime import datetime
from colorama import Fore, init

init(autoreset=True)  # Enable color output on Windows too

def scan_ports(target, start_port, end_port):
    print(f"\n🔍 Scanning target: {target}")
    print(f"⏳ Time started: {datetime.now()}")
    
    try:
        for port in range(start_port, end_port + 1):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1)
            result = s.connect_ex((target, port))
            if result == 0:
                print(Fore.GREEN + f"[+] Port {port} is open")
            else:
                print(Fore.RED + f"[-] Port {port} is closed")
            s.close()
    except KeyboardInterrupt:
        print(Fore.YELLOW + "\n❌ Scan interrupted by user.")
    except socket.gaierror:
        print(Fore.RED + "❗ Hostname could not be resolved.")
    except socket.error:
        print(Fore.RED + "❗ Couldn't connect to server.")

def main():
    print(Fore.CYAN + "🔐 Welcome to CyberScan Port Scanner 🔐")
    target = input("Enter target IP or domain: ")
    start_port = int(input("Start Port: "))
    end_port = int(input("End Port: "))
    scan_ports(target, start_port, end_port)

if __name__ == "__main__":
    main()
