#!/usr/bin/python3
import sys

total_size = 0 
status_counts = {}
valid_codes =  200, 301, 400, 401, 403, 404, 405, 500
line_count = 0

def print_stats():
    """Prints the total size and the status code counts."""
    print(f"File size: {total_size}")
    for code in sorted(status_counts):
        if status_counts[code] > 0:
            print(f"{code}: {status_counts[code]}")
            
try:
    for line in sys.stdin:
        parts = line.split()
        if len(parts) <7:
            continue
        
        try:
            status_code = int(parts[-2])
            file_size = int(parts[-1])
        except ValueError:
            continue
        
        total_size +=file_size
        
        if status_code in valid_codes:
            status_counts[status_code] = status_counts.get(status_code, 0) + 1
        line_count += 1
        if line_count % 10 == 0:
            print_stats()

except KeyboardInterrupt:
    print_stats()
    sys.exit(0)
            
        