Python 3.14.3 (v3.14.3:323c59a5e34, Feb  3 2026, 11:41:37) [Clang 16.0.0 (clang-1600.0.26.6)] on darwin
Enter "help" below or click "Help" above for more information.
import psutil
import platform
import socket
import time
from datetime import datetime

def get_system_info():
    print("=== SYSTEM INFORMATION ===")
    print(f"System: {platform.system()}")
    print(f"Node Name: {platform.node()}")
    print(f"Release: {platform.release()}")
    print(f"Version: {platform.version()}")
    print(f"Machine: {platform.machine()}")
    print(f"Processor: {platform.processor()}")
    print()

def get_network_info():
    print("=== NETWORK INFORMATION ===")
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)
    print(f"Hostname: {hostname}")
    print(f"IP Address: {ip}")
    print()

def get_cpu_info():
    cpu = psutil.cpu_percent(interval=1)
    print("=== CPU USAGE ===")
    print(f"CPU Usage: {cpu}%")

    if cpu > 80:
        print("⚠️ WARNING: High CPU usage!")

    print()

def get_memory_info():
    memory = psutil.virtual_memory()
    print("=== MEMORY USAGE ===")
    print(f"Total: {round(memory.total / (1024**3), 2)} GB")
    print(f"Used: {round(memory.used / (1024**3), 2)} GB")
    print(f"Usage: {memory.percent}%")

    if memory.percent > 80:
        print("⚠️ WARNING: High memory usage!")

    print()

def get_disk_info():
    disk = psutil.disk_usage('/')
    print("=== DISK USAGE ===")
    print(f"Total: {round(disk.total / (1024**3), 2)} GB")
    print(f"Used: {round(disk.used / (1024**3), 2)} GB")
    print(f"Free: {round(disk.free / (1024**3), 2)} GB")
    print(f"Usage: {disk.percent}%")

    if disk.percent > 80:
        print("⚠️ WARNING: Low disk space!")

    print()

def get_top_processes():
    print("=== TOP PROCESSES (by CPU) ===")
...     processes = []
... 
...     for proc in psutil.process_iter(['pid', 'name', 'cpu_percent']):
...         processes.append(proc.info)
... 
...     processes = sorted(processes, key=lambda x: x['cpu_percent'], reverse=True)[:5]
... 
...     for p in processes:
...         print(f"PID: {p['pid']} | Name: {p['name']} | CPU: {p['cpu_percent']}%")
... 
...     print()
... 
... def save_report():
...     with open("system_report.txt", "w") as f:
...         f.write(f"System Report - {datetime.now()}\n")
...         f.write(f"CPU Usage: {psutil.cpu_percent()}%\n")
...         mem = psutil.virtual_memory()
...         f.write(f"Memory Usage: {mem.percent}%\n")
...         disk = psutil.disk_usage('/')
...         f.write(f"Disk Usage: {disk.percent}%\n")
... 
...     print("Report saved to system_report.txt\n")
... 
... def main():
...     print("🔍 SYSTEM HEALTH CHECKER\n")
... 
...     get_system_info()
...     get_network_info()
...     get_cpu_info()
...     get_memory_info()
...     get_disk_info()
...     get_top_processes()
... 
...     save = input("Save report? (y/n): ").lower()
...     if save == "y":
...         save_report()
... 
... if __name__ == "__main__":
