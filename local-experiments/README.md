# Local experiments (no Kubernetes)

These scripts let you run simple chaos-like tests on your local machine (Windows).
Use them carefully — they consume CPU, memory, disk or may kill processes.

Prerequisites
- Python 3.8+

Quick examples (PowerShell):

Run CPU stress for 60 seconds using 2 workers:
```powershell
python .\local-experiments\run.py cpu --workers 2 --duration 60
```

Fill ~1 GB RAM for 45 seconds:
```powershell
python .\local-experiments\run.py memory --size 1G --duration 45
```

Create a 1.5 GB temp file in current folder:
```powershell
python .\local-experiments\run.py disk --size 1.5G --path .\disk_fill.tmp
```

Kill a process by PID (Windows):
```powershell
python .\local-experiments\run.py kill --pid 12345
```

Send repeated requests with client-side delay to simulate latency (useful if your app is running locally):
```powershell
python .\local-experiments\run.py http-delay --url http://localhost:5000/health --count 20 --delay 0.5
```

Safety notes
- Stop scripts with Ctrl+C.
- Do not run memory/disk fills on systems where you don't want resources consumed.

Run GUI without console (Windows)
--------------------------------

If you prefer not to use the terminal, double-click `run-launcher.bat` in the project root. The batch file will try to use `pythonw` (no console window). If `pythonw` is not available on your PATH it will fall back to `python` (a console may appear).

Alternatively, run `pythonw` explicitly:

```powershell
C:\> pythonw .\local-experiments\launcher.py
```

Logs from GUI-launched experiments are stored in `local-experiments/launcher-logs/`.
