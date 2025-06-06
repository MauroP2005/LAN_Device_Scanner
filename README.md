# LAN Device Scanner

A Python tool that scans your local network and lists all connected devices. Useful for identifying unknown devices, auditing your home or office network, or learning how subnet scanning works.

---

## Features

- Detects your local IP address and subnet mask
- Calculates your network's CIDR range (e.g. `192.168.1.0/24`)
- Scans all devices on the subnet using multithreaded ping
- [Planned] Displays hostname and MAC address (if available)

---

## Requirements

- Python 3.10+
- `psutil` package

### Install requirements:
```bash
pip install psutil
