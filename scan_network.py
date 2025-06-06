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
    return result.returncode

def scan_subnet(network):
    """
    Placeholder function to ping all IPs in the subnet
    """
    print(f"Scanning subnet: {network}")

if __name__ == "__main__":
    _, _, subnet = get_local_network_info()
    scan_subnet(subnet)