from network_info import get_local_network_info

def scan_subnet(network):
    """
    Placeholder function to ping all IPs in the subnet
    """
    print(f"Scanning subnet: {network}")

if __name__ == "__main__":
    _, _, subnet = get_local_network_info()
    scan_subnet(subnet)