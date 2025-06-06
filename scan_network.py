import subprocess
from network_info import get_local_network_info

def ping(ip):
    """
    Attempts to ping an IP once.
    """
    result = subprocess.run(
        ["ping", "-n", "1", ip],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )
    return result.returncode == 0

def scan_subnet(network):
    print(f"Scanning subnet: {network}")
    for ip in network.hosts():
        if ping(str(ip)):
            print(f"[*] {ip} is online")
            
if __name__ == "__main__":
    _, _, subnet = get_local_network_info()
    scan_subnet(subnet)