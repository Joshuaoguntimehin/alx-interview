#!/usr/bin/python3
import sys

# Initialize total file size and status code counts
total_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0  # To track every 10 lines


def print_stats():
    """Prints the statistics collected so far."""
    print(f"File size: {total_size}")
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")


try:
    for line in sys.stdin:
        parts = line.split()

        # Validate and parse the line according to the expected format
        if len(parts) < 7:
            continue  # Skip malformed lines

        try:
            status_code = int(parts[-2])
            file_size = int(parts[-1])
        except ValueError:
            continue  # Skip lines with invalid status code or file size

        # Update total size and status code counts
        total_size += file_size
        if status_code in status_codes:
            status_codes[status_code] += 1

        line_count += 1

        # Print stats every 10 lines
        if line_count % 10 == 0:
            print_stats()

except KeyboardInterrupt:
    # Handle keyboard interruption gracefully
    print_stats()
    sys.exit(0)  # Exit cleanly
