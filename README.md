# LAN Device Scanner

![Python](https://img.shields.io/badge/python-3.11+-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Last Commit](https://img.shields.io/github/last-commit/MauroP2005/LAN_Device_Scanner)
![Repo Size](https://img.shields.io/github/repo-size/MauroP2005/LAN_Device_Scanner)
![Release](https://img.shields.io/github/v/release/MauroP2005/LAN_Device_Scanner?label=version)

A Python tool that scans your local network and lists all connected devices. Useful for identifying unknown devices, auditing your home or office network, or learning how subnet scanning works.

> This was my first full GitHub project — built to learn Python scripting, network scanning, and real-world version control workflows.
---

## Features

- Detects your local IP address and subnet mask
- Calculates your network's CIDR range (e.g. `192.168.1.0/24`)
- Scans all devices on the subnet using multithreaded ping
- Resolves hostnames via reverse DNS
- Exports results to `scan_results.csv`
- Handles unreachable hostnames safely (no crashes)

---

## Requirements

- Python 3.10+
- `psutil` package

### Install requirements:
```bash
pip install psutil
```

---

## Example Output

```bash
Scanning subnet: 192.168.0.0/24
[*] 192.168.0.1 is online (Router)
[*] 192.168.0.10 is online (Mauro-Laptop)
[*] 192.168.0.12 is online (Galaxy-S23)
[*] 192.168.0.15 is online (HP-Printer)
[*] 192.168.0.23 is online (Nest-Thermostat)
[*] 192.168.0.42 is online (LivingRoom-TV)
[*] 192.168.0.58 is online (Unknown)

Scan complete. 7 devices found!