import subprocess
import platform

def ping(host):
    param = '-n' if platform.system().lower()=='windows' else '-c'
    command = ['ping', param, '4', host]
    try:
        output = subprocess.check_output(command).decode()
        print(output)
    except:
        print(f"Gagal terhubung ke {host}")

# Daftar target server global
targets = {
    "UNP (Lokal Padang)": "unp.ac.id",
    "Singapore (Asia)": "sgp-ping.vultr.com",
    "United States (US)": "nj-ping.vultr.com",
    "London (Europe)": "lon-ping.vultr.com"
}

for name, host in targets.items():
    print(f"\n--- Testing Latency to {name} ({host}) ---")
    ping(host)
