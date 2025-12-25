import sys
import os
import subprocess
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from pathlib import Path

ROOT = Path(__file__).parent

class Launcher(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Local Experiments Launcher')
        self.geometry('520x320')
        self.processes = []

        frm = ttk.Frame(self, padding=12)
        frm.pack(fill='both', expand=True)

        ttk.Label(frm, text='Select experiment and click Run (no terminal required)').pack(pady=(0,8))

        # CPU
        cpu_frame = ttk.LabelFrame(frm, text='CPU Stress')
        cpu_frame.pack(fill='x', pady=6)
        ttk.Label(cpu_frame, text='Workers:').grid(row=0, column=0, sticky='w')
        self.cpu_workers = tk.StringVar(value='1')
        ttk.Entry(cpu_frame, width=6, textvariable=self.cpu_workers).grid(row=0, column=1)
        ttk.Label(cpu_frame, text='Duration(s):').grid(row=0, column=2, sticky='w')
        self.cpu_duration = tk.StringVar(value='30')
        ttk.Entry(cpu_frame, width=6, textvariable=self.cpu_duration).grid(row=0, column=3)
        ttk.Button(cpu_frame, text='Run', command=self.run_cpu).grid(row=0, column=4, padx=8)

        # Memory
        mem_frame = ttk.LabelFrame(frm, text='Memory Stress')
        mem_frame.pack(fill='x', pady=6)
        ttk.Label(mem_frame, text='Size:').grid(row=0, column=0, sticky='w')
        self.mem_size = tk.StringVar(value='512M')
        ttk.Entry(mem_frame, width=8, textvariable=self.mem_size).grid(row=0, column=1)
        ttk.Label(mem_frame, text='Duration(s):').grid(row=0, column=2, sticky='w')
        self.mem_duration = tk.StringVar(value='30')
        ttk.Entry(mem_frame, width=6, textvariable=self.mem_duration).grid(row=0, column=3)
        ttk.Button(mem_frame, text='Run', command=self.run_memory).grid(row=0, column=4, padx=8)

        # Disk
        disk_frame = ttk.LabelFrame(frm, text='Disk Fill')
        disk_frame.pack(fill='x', pady=6)
        ttk.Label(disk_frame, text='Size:').grid(row=0, column=0, sticky='w')
        self.disk_size = tk.StringVar(value='500M')
        ttk.Entry(disk_frame, width=8, textvariable=self.disk_size).grid(row=0, column=1)
        ttk.Label(disk_frame, text='Path:').grid(row=0, column=2, sticky='w')
        self.disk_path = tk.StringVar(value=str(ROOT / 'disk_fill.tmp'))
        ttk.Entry(disk_frame, width=24, textvariable=self.disk_path).grid(row=0, column=3)
        ttk.Button(disk_frame, text='Run', command=self.run_disk).grid(row=0, column=4, padx=8)

        # HTTP delay
        http_frame = ttk.LabelFrame(frm, text='HTTP Delay Client')
        http_frame.pack(fill='x', pady=6)
        ttk.Label(http_frame, text='URL:').grid(row=0, column=0, sticky='w')
        self.http_url = tk.StringVar(value='http://localhost:5000/health')
        ttk.Entry(http_frame, width=28, textvariable=self.http_url).grid(row=0, column=1, columnspan=2)
        ttk.Label(http_frame, text='Count:').grid(row=0, column=3, sticky='w')
        self.http_count = tk.StringVar(value='10')
        ttk.Entry(http_frame, width=6, textvariable=self.http_count).grid(row=0, column=4)
        ttk.Button(http_frame, text='Run', command=self.run_http).grid(row=0, column=5, padx=8)

        # Controls
        ctrl = ttk.Frame(frm)
        ctrl.pack(fill='x', pady=8)
        ttk.Button(ctrl, text='Stop All', command=self.stop_all).pack(side='left')
        ttk.Button(ctrl, text='Open Logs Folder', command=self.open_logs).pack(side='left', padx=8)

        self.logdir = ROOT / 'launcher-logs'
        self.logdir.mkdir(exist_ok=True)

    def _start_script(self, script: Path, args: list):
        py = sys.executable
        cmd = [py, str(script)] + args
        logfile = self.logdir / f"{script.stem}-{len(self.processes)+1}.log"
        f = open(logfile, 'ab')
        kwargs = {}
        if os.name == 'nt':
            kwargs['creationflags'] = subprocess.CREATE_NO_WINDOW
        p = subprocess.Popen(cmd, stdout=f, stderr=subprocess.STDOUT, close_fds=True, **kwargs)
        self.processes.append((p, f))
        messagebox.showinfo('Started', f'Started {script.name} (pid={p.pid})\nLog: {logfile}')

    def run_cpu(self):
        script = ROOT / 'cpu_stress.py'
        args = ['--workers', self.cpu_workers.get(), '--duration', self.cpu_duration.get()]
        self._start_script(script, args)

    def run_memory(self):
        script = ROOT / 'memory_stress.py'
        args = ['--size', self.mem_size.get(), '--duration', self.mem_duration.get()]
        self._start_script(script, args)

    def run_disk(self):
        script = ROOT / 'disk_fill.py'
        args = ['--size', self.disk_size.get(), '--path', self.disk_path.get()]
        self._start_script(script, args)

    def run_http(self):
        script = ROOT / 'http_delay_client.py'
        args = ['--url', self.http_url.get(), '--count', self.http_count.get(), '--delay', '0.2']
        self._start_script(script, args)

    def stop_all(self):
        stopped = 0
        for p, f in list(self.processes):
            try:
                p.terminate()
                p.wait(timeout=2)
            except Exception:
                try:
                    p.kill()
                except Exception:
                    pass
            try:
                f.close()
            except Exception:
                pass
            self.processes.remove((p, f))
            stopped += 1
        messagebox.showinfo('Stopped', f'Stopped {stopped} processes')

    def open_logs(self):
        path = str(self.logdir)
        if os.name == 'nt':
            os.startfile(path)
        else:
            subprocess.Popen(['xdg-open', path])

if __name__ == '__main__':
    app = Launcher()
    app.mainloop()
