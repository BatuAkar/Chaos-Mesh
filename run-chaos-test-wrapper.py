import os
import sys
import subprocess

here = os.path.dirname(__file__)
script = os.path.join(here, 'chaos-test-simple.py')
report = os.path.join(here, 'chaos-test-report.txt')

def main():
    try:
        with open(report, 'w', encoding='utf-8') as f:
            p = subprocess.Popen([sys.executable, script], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
            for line in p.stdout:
                f.write(line)
            p.wait()
    except Exception as e:
        try:
            with open(report, 'a', encoding='utf-8') as f:
                f.write('\nERROR: ' + str(e) + '\n')
        except Exception:
            pass
    # try to open the report (works on Windows)
    try:
        os.startfile(report)
    except Exception:
        pass

if __name__ == '__main__':
    main()
