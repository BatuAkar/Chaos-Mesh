import time
import argparse
import multiprocessing

def worker(duration):
    end = time.time() + duration
    # busy loop
    while time.time() < end:
        x = 0
        for i in range(10000):
            x += i*i

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--workers', type=int, default=multiprocessing.cpu_count(), help='Number of worker processes')
    parser.add_argument('--duration', type=int, default=60, help='Duration in seconds')
    args = parser.parse_args()

    procs = []
    for _ in range(args.workers):
        p = multiprocessing.Process(target=worker, args=(args.duration,))
        p.start()
        procs.append(p)

    try:
        for p in procs:
            p.join()
    except KeyboardInterrupt:
        for p in procs:
            p.terminate()

if __name__ == '__main__':
    main()
