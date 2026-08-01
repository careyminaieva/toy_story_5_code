import argparse, socket
import subprocess
from eggman.pondnet import traceutils


def get_ip_address(url):
    try:
        # Extract hostname from URL
        print(f"Resolving server for {url}")
        hostname = url.split("://")[-1].split("/")[0]

        print(f"Resolving IP address of {hostname}...")
        ip_address = socket.gethostbyname(hostname)

        print(f"IP address of {hostname}: {ip_address}")
        return ip_address

    except socket.gaierror:
        print(f"Could not resolve IP address for {url}")
        return None
