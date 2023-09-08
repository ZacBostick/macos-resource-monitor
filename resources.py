import psutil
import tkinter as tk
from tkinter import ttk
import datetime

def get_detailed_cpu_usage():
    """Returns a string containing the CPU usage percentage for each core."""
    per_core_usage = psutil.cpu_percent(interval=1, percpu=True)
    usage_strings = [f"Core {i+1}: {usage}%" for i, usage in enumerate(per_core_usage)]
    return ", ".join(usage_strings)

def get_cpu_usage():
    return psutil.cpu_percent(interval=1)

def get_ram_usage():
    ram = psutil.virtual_memory()
    return ram.percent

def get_storage_usage():
    partitions = psutil.disk_partitions()
    main_partition = [p for p in partitions if p.mountpoint == '/'][0]
    usage = psutil.disk_usage(main_partition.mountpoint)
    return usage.percent
def get_uptime():
    boot_timestamp = psutil.boot_time()
    boot_datetime = datetime.datetime.fromtimestamp(boot_timestamp)
    delta = datetime.datetime.now() - boot_datetime
    return str(delta).split('.')[0]  

def get_network_info():
    net_info = psutil.net_io_counters()
    sent = round(net_info.bytes_sent / (1024*1024), 2)
    received = round(net_info.bytes_recv / (1024*1024), 2)
    return f"Sent: {sent} MB, Received: {received} MB"

def get_battery_info():
    battery = psutil.sensors_battery()
    if battery:
        plugged = "Plugged" if battery.power_plugged else "Not Plugged"
        return f"{battery.percent}% | {plugged}"
    else:
        return "No Battery Info Available"

def get_temperature_info():
    try:
        temp_info = psutil.sensors_temperatures()
        if 'coretemp' in temp_info:
            core_temp = temp_info['coretemp']
            if core_temp:
                return f"{core_temp[0].current}°C"
    except AttributeError:
        pass

    return "No Temp Info Available"
def update_stats_with_alerts():
    cpu_usage = get_cpu_usage()
    ram_usage = get_ram_usage()
    storage_usage = get_storage_usage()

    cpu_label.config(text=f"CPU Usage: {cpu_usage}%")
    ram_label.config(text=f"RAM Usage: {ram_usage}%")
    storage_label.config(text=f"Storage Usage: {storage_usage}%")
    
    uptime_label.config(text=f"Uptime: {get_uptime()}")
    network_label.config(text=f"Network: {get_network_info()}")
    battery_label.config(text=f"Battery: {get_battery_info()}")
    temperature_label.config(text=f"Temperature: {get_temperature_info()}")
    
    root.after(5000, update_stats_with_alerts)
root = tk.Tk()
root.title("Resource Monitor")

style = ttk.Style()
style.configure("TLabel", font=("Arial", 12))

root.geometry("350x200")
root.resizable(True, True)  
frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

for i in range(7):
    frame.grid_rowconfigure(i, weight=1)
frame.grid_columnconfigure(0, weight=1)

root.wm_attributes('-topmost', 1) 

frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))


for i in range(7):
    frame.grid_rowconfigure(i, weight=1)
frame.grid_columnconfigure(0, weight=1)


cpu_label = ttk.Label(frame)
cpu_label.grid(row=0, column=0, sticky=tk.W, pady=5)

ram_label = ttk.Label(frame)
ram_label.grid(row=1, column=0, sticky=tk.W, pady=5)

storage_label = ttk.Label(frame)
storage_label.grid(row=2, column=0, sticky=tk.W, pady=5)

uptime_label = ttk.Label(frame)
uptime_label.grid(row=3, column=0, sticky=tk.W, pady=5)

network_label = ttk.Label(frame)
network_label.grid(row=4, column=0, sticky=tk.W, pady=5)

battery_label = ttk.Label(frame)
battery_label.grid(row=5, column=0, sticky=tk.W, pady=5)

temperature_label = ttk.Label(frame)
temperature_label.grid(row=6, column=0, sticky=tk.W, pady=5)

update_stats_with_alerts()

root.mainloop()



