#!/usr/bin/python3
"""Log parsing"""
import sys


status_codes = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0,
}
line_cnt = 0
total_size = 0


def print_stats():
    print("File size: {:d}".format(total_size))
    for key, value in status_codes.items():
        if value:
            print("{}: {:d}".format(key, value))


try:
    for line in sys.stdin:
        line_cnt += 1
        line = line[:-1]
        array = line.split()
        file_size = 0
        try:
            file_size = int(array[-1])
        except:
            pass

        total_size += file_size
        try:
            status_code = str(array[-2])
            if status_code in status_codes:
                status_codes[status_code] += 1
        except:
            pass

        if (line_cnt % 10 == 0):
            print_stats()
    print_stats()
except KeyboardInterrupt:
    print_stats()
    raise
