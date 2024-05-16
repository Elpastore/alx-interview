#!/usr/bin/python3
"""
0-stats module
"""
import re
import sys


def get_input(line):
    """
    get the input
    """
    pattern = r'^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - \[(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{6})\] "GET \/projects\/260 HTTP\/1\.1" (\d{3}) (\d+)$'
    match = re.match(pattern, line)
    
    information = {}
    
    if match:
        ip_address = match.group(1)
        date = match.group(2)
        status_code = int(match.group(3))
        file_size = int(match.group(4))
        
        information['File Size'] = file_size
        information['Status Code'] = status_code
        
        return information
    else:
        print("Input string does not match the expected format.")

if __name__ == "__main__":
    total_size = 0
    status_counts = {'200': 0, '301': 0, '400': 0, '401': 0,
                     '403': 0, '404': 0, '405': 0, '500': 0}
    line_counter = 0

    try:
        for line in sys.stdin:
            information = get_input(line)
            
            if information:
                status_code = str(information.get('Status Code'))
                total_size += information.get('File Size')
                status_counts[status_code] += 1
                line_counter += 1
                
                if line_counter % 10 == 0:
                    print(f"Total file size: {total_size}")
                    for code, count in sorted(status_counts.items()):
                        if count > 0:
                            print(f"{code}: {count}")
                    #print()
                    line_counter = 0

    #except KeyboardInterrupt:
    except (KeyboardInterrupt, EOFError):
        print(f"Total file size: {total_size}")
        for code, count in sorted(status_counts.items()):
            if count > 0:
                print(f"{code}: {count}")
