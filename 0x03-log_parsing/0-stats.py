#!/usr/bin/python3
"""
0-stats module
"""
import re


def get_input(input_line):
    """get the iput in the right format."""
    pattern_parts = (
        r'\s*(?P<ip>\S+)\s*',
        r'\s*\[(?P<date>\d+\-\d+\-\d+ \d+:\d+:\d+\.\d+)\]',
        r'\s*"(?P<request>[^"]*)"\s*',
        r'\s*(?P<status_code>\S+)',
        r'\s*(?P<file_size>\d+)'
    )
    pattern = '{}\\-{}{}{}{}\\s*'.format(*pattern_parts)
    match = re.fullmatch(pattern, input_line)
    if match:
        status_code = match.group('status_code')
        file_size = int(match.group('file_size'))
        return {'status_code': status_code, 'file_size': file_size}
    return {'status_code': 0, 'file_size': 0}


def print_statistics(total_file_size, status_codes_stats):
    """
    Print the statistical info
    """
    print('Total file size:', total_file_size)
    for status_code in sorted(status_codes_stats.keys()):
        num = status_codes_stats.get(status_code, 0)
        if num > 0:
            print(f'{status_code}: {num}')


def update_metrics(line, total_file_size, status_codes_stats):
    """
    Updates information
    """
    line_info = get_input(line)
    status_code = line_info.get('status_code', '0')
    if status_code in status_codes_stats:
        status_codes_stats[status_code] += 1
    return total_file_size + line_info['file_size']


def main():
    """
    executor
    """
    line_num = 0
    total_file_size = 0
    status_codes_stats = {'200': 0,
                          '301': 0,
                          '400': 0,
                          '401': 0,
                          '403': 0,
                          '404': 0,
                          '405': 0,
                          '500': 0
                          }
    try:
        while True:
            line = input()
            total_file_size = update_metrics(
                line, total_file_size, status_codes_stats)
            line_num += 1
            if line_num % 10 == 0:
                print_statistics(total_file_size, status_codes_stats)
    except (KeyboardInterrupt, EOFError):
        print_statistics(total_file_size, status_codes_stats)


if __name__ == '__main__':
    main()
