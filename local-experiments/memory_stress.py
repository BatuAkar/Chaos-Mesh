import argparse
import time

def allocate_bytes(target_bytes, duration):
    # allocate in chunks to avoid freezing the interpreter too long
    chunk = 10 * 1024 * 1024  # 10MiB
    blocks = []
    allocated = 0
    try:
        while allocated < target_bytes and duration > 0:
            blocks.append(bytearray(chunk))
            allocated += chunk
            time.sleep(0.01)
        # hold for duration
        time.sleep(duration)
    except MemoryError:
        print('MemoryError: allocated up to', allocated)
    finally:
        blocks.clear()

def parse_size(s):
    s = s.strip().upper()
    if s.endswith('G'):
        return int(float(s[:-1]) * 1024**3)
    if s.endswith('M'):
        return int(float(s[:-1]) * 1024**2)
    return int(s)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--size', default='1G', help='Target allocation size (e.g. 512M, 1G)')
    parser.add_argument('--duration', type=int, default=60, help='Duration in seconds to hold allocation')
    args = parser.parse_args()

    target = parse_size(args.size)
    print(f'Allocating ~{args.size} for {args.duration}s')
    allocate_bytes(target, args.duration)

if __name__ == '__main__':
    main()
