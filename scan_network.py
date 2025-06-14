import subprocess
from network_info import get_local_network_info
from concurrent.futures import ThreadPoolExecutor
import socket
import csv

def ping(ip):
    """
    Attempts to ping an IP once.
    Suppresses output and returns True if host responds.
    """
    result = subprocess.run(
        ["ping", "-n", "1", "-w", "100", ip],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )
    return result.returncode == 0

def resolve_hostname(ip):
    #Reverse DNS lookup on the given IP address
    try:
        return socket.gethostbyaddr(ip)[0]
    except socket.herror:
        return "Unknown"

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
            hostname = resolve_hostname(str(ip))    #Get hostname
            print(f"[*] {ip} is online")
            alive_hosts.append((str(ip), hostname))   #Store IP and host name
    
    print(f"\nScan complete. {len(alive_hosts)} devices found!")
    return alive_hosts

def save_results(alive_hosts, filename="scan_results.csv"):
    with open(filename, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["IP Address", "Hostname"])
        for ip, hostname in alive_hosts:
            writer.writerow([ip, hostname])

if __name__ == "__main__":
    _, _, subnet = get_local_network_info()
    results = scan_subnet(subnet)       #Scan subnet for live devices and resolve their hostnames
    save_results(results)  #Include only if using CSV export