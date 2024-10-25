#!/usr/bin/python3
"""import statement"""
import sys
from signal import signal, SIGINT

# Initialize metrics
total_file_size = 0
status_counts = {code: 0 for code in [200, 301, 400, 401, 403, 404, 405, 500]}
line_count = 0

def print_stats():
    """Print the statistics collected so far."""
    print(f"File size: {total_file_size}")
    for code in sorted(status_counts):
        if status_counts[code] > 0:
            print(f"{code}: {status_counts[code]}")

def handle_exit(signal_received, frame):
    """Handle keyboard interruption (CTRL + C)."""
    print_stats()
    sys.exit(0)

# Register SIGINT handler for graceful exit
signal(SIGINT, handle_exit)

try:
    for line in sys.stdin:
        parts = line.split()
        # Ensure the line format matches the expected structure
        if len(parts) < 7:
            continue

        try:
            # Extract relevant parts from the line
            ip_address = parts[0]
            date = parts[3] + " " + parts[4]
            method = parts[5][1:]
            path = parts[6]
            status_code = int(parts[-2])
            file_size = int(parts[-1])

            # Validate method and path
            if method != "GET" or path != "/projects/260":
                continue

            # Update metrics
            total_file_size += file_size
            if status_code in status_counts:
                status_counts[status_code] += 1

            line_count += 1

            # Print statistics after every 10 lines
            if line_count % 10 == 0:
                print_stats()
        except (ValueError, IndexError):
            # Skip lines with parsing errors
            continue

    # Print remaining statistics at the end
    print_stats()

except KeyboardInterrupt:
    # Handle CTRL + C
    print_stats()
    sys.exit(0)
