import argparse
import time
import urllib.request

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--url', required=True, help='URL to request')
    parser.add_argument('--count', type=int, default=10, help='Number of requests')
    parser.add_argument('--delay', type=float, default=0.2, help='Delay between requests in seconds')
    args = parser.parse_args()

    for i in range(args.count):
        try:
            start = time.time()
            resp = urllib.request.urlopen(args.url, timeout=10)
            body = resp.read(200)
            elapsed = time.time() - start
            print(f'{i+1}/{args.count} -> {args.url}  status={resp.getcode()} time={elapsed:.3f}s')
        except Exception as e:
            print(f'{i+1}/{args.count} -> ERROR: {e}')
        time.sleep(args.delay)

if __name__ == '__main__':
    main()
