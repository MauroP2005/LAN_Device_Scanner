import subprocess
from network_info import get_local_network_info
from concurrent.futures import ThreadPoolExecutor

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
    """
    Scans subnet using multiple threads for faster pinging.
    """
    print(f"Scanning subnet: {network}")
    alive_hosts = []
    hosts = list(network.hosts())
    
    with ThreadPoolExecutor(max_workers=100) as executor:
        results = executor.map(ping, map(str, hosts))
        
    for ip, is_alive in  zip(hosts, results):
        if is_alive:    
            print(f"[*] {ip} is online")
            alive_hosts.append(str(ip))
    
    print(f"\nScan complete. {len(alive_hosts)} devices found!")
    return alive_hosts
    
if __name__ == "__main__":
    _, _, subnet = get_local_network_info()
    scan_subnet(subnet)