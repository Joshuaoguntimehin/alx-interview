#!/usr/bin/python3
"""importstatement"""
import sys
import re
"""import statement"""


def initialize_log():
    """Initialize the metrics."""
    status_codes = {200, 301, 400, 401, 403, 404, 405, 500}
    log = {
        "file_size": 0,
        "code_list": {str(code): 0 for code in status_codes}
    }
    return log


def parse_line(line, regex, log):
    """Parse each line and update log metrics."""
    match = regex.match(line)

    if match:
        stat_code, file_size = match.group(1, 2)
        log["file_size"] += int(file_size)

        if stat_code in log["code_list"]:
            log["code_list"][stat_code] += 1


def print_log(log):
    """Print the accumulated log metrics."""
    print("File size: {}".format(log['file_size']))

    sorted_codes = sorted(log["code_list"].items())
    for code, count in sorted_codes:
        if count > 0:
            print(f"{code}: {count}")


def main():
    """Main function to process input lines."""
    regex = re.compile(
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} - '
        r'\[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d+\] '
        r'"GET /projects/260 HTTP/1\.1" (\d{3}) (\d+)'
    )

    log = initialize_log()
    line_count = 0

    try:
        for line in sys.stdin:
            line = line.strip()
            parse_line(line, regex, log)
            line_count += 1

            if line_count % 10 == 0:
                print_log(log)

    except KeyboardInterrupt:
        print_log(log)
        raise

    print_log(log)


if __name__ == "__main__":
    main()
