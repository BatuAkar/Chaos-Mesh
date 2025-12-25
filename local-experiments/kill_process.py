import argparse
import os
import signal
import subprocess

def kill_pid(pid):
    try:
        if os.name == 'nt':
            subprocess.check_call(['taskkill', '/PID', str(pid), '/F'])
        else:
            os.kill(pid, signal.SIGKILL)
        print('Killed PID', pid)
    except Exception as e:
        print('Failed to kill PID', pid, e)

def kill_by_name(name):
    try:
        if os.name == 'nt':
            subprocess.check_call(['taskkill', '/IM', name, '/F'])
            print('Requested kill by name', name)
        else:
            # use pkill
            subprocess.check_call(['pkill', '-f', name])
            print('Requested kill by name', name)
    except Exception as e:
        print('Failed to kill by name', name, e)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--pid', type=int, help='Process id to kill')
    parser.add_argument('--name', help='Process image/name to kill (e.g. python.exe)')
    args = parser.parse_args()

    if args.pid:
        kill_pid(args.pid)
    elif args.name:
        kill_by_name(args.name)
    else:
        print('Specify --pid or --name')

if __name__ == '__main__':
    main()
