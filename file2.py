def launch_gps_tracker(ip_address):
    try:
        print(f"LAUNCHING GPS TRACKER for {ip_address}")
        result = subprocess.run([traceutils.gps_tracker, ip_address],
                                capture_output=True, text=True, check=True
        )
        print(result.stdout)

    except FileNotFoundError:
        print("Error: gps-tracker program not found.")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
