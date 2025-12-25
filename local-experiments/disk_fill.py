import argparse
import os

def parse_size(s):
    s = s.strip().upper()
    if s.endswith('G'):
        return int(float(s[:-1]) * 1024**3)
    if s.endswith('M'):
        return int(float(s[:-1]) * 1024**2)
    return int(s)

def fill_file(path, size_bytes):
    written = 0
    chunk = 4 * 1024 * 1024
    with open(path, 'wb') as f:
        while written < size_bytes:
            to_write = min(chunk, size_bytes - written)
            f.write(b'0' * to_write)
            written += to_write
    print(f'Wrote {written} bytes to {path}')

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--size', default='1G', help='Size to write (e.g. 500M, 1.5G)')
    parser.add_argument('--path', default='disk_fill.tmp', help='File path to create')
    args = parser.parse_args()

    size = parse_size(args.size)
    if os.path.exists(args.path):
        print('Removing existing file', args.path)
        os.remove(args.path)
    fill_file(args.path, size)

if __name__ == '__main__':
    main()
