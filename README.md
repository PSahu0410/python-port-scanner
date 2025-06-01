# Basic Python Port Scanner

A simple command-line port scanner built with Python.  
It scans a range of TCP ports on a target IP or hostname and reports open ports along with their common service names.

---

## Features

- Scan any range of ports using command-line arguments (`-s` for start port, `-e` for end port)
- Supports both IP addresses and domain names as targets (`-t` argument)
- Outputs results to console and logs them in `Port_Scanner.txt`
- Attempts to identify the standard service running on each open port
- Shows start time, end time, and total time taken for the scan

---

## Requirements

- Python 3.x (no external packages required)

---

## Usage

Run the script from your terminal or command prompt:

```bash
python port.py -t <target_ip_or_hostname> -s <start_port> -e <end_port>
