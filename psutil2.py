import psutil

# Get CPU usage
cpu_usage = psutil.cpu_percent(interval=1)  # You can adjust the interval as needed
print(f"CPU Usage: {cpu_usage}%")

# Get the number of CPU cores
num_cores = psutil.cpu_count(logical=False)  # Physical cores
num_logical_cores = psutil.cpu_count(logical=True)  # Logical cores (including hyper-threading)

print(f"Number of CPU Cores: {num_cores} (Physical)")
print(f"Number of Logical CPU Cores: {num_logical_cores} (Including Hyper-Threading)")