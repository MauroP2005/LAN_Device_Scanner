import socket
import psutil
import ipaddress

def get_local_network_info():
    """
    Gets local IP address, subnet mask, and computes network range (CIDR).
    Returns a tuple: (ip_address, subnet_mask, network_range)
    """
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)

    for interface, addrs in psutil.net_if_addrs().items():
        for addr in addrs:
            if addr.family == socket.AF_INET and addr.address == local_ip:
                subnet_mask = addr.netmask
                network = ipaddress.IPv4Interface(f"{local_ip}/{subnet_mask}").network
                return local_ip, subnet_mask, network

    raise RuntimeError("Could not determine local network info.")

# Run this code if this file is executed directly
if __name__ == "__main__":
    ip, mask, net = get_local_network_info()
    print(f"Local IP Address: {ip}")
    print(f"Subnet Mask: {mask}")
    print(f"Network Range (CIDR): {net}")
