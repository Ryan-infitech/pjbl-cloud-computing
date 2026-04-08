import os
import time
import platform
import subprocess
import sys

# --- 1. AUTO-INSTALLER ENGINE ---
def install_and_import(package):
    try:
        __import__(package)
    except ImportError:
        print(f"[SYSTEM] Module '{package}' tidak ditemukan. Menginstal...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# Pastikan library krusial tersedia
for pkg in ['psutil', 'numpy', 'tqdm', 'tabulate']:
    install_and_import(pkg)

import psutil
import numpy as np
from tqdm import tqdm
from tabulate import tabulate

# --- 2. DETEKSI IDENTITAS INFRASTRUKTUR ---
is_colab = 'COLAB_RELEASE_TAG' in os.environ
env_label = "☁️  GOOGLE COLAB (CLOUD)" if is_colab else "💻 LOCAL MACHINE (VS CODE)"

def get_cpu_info():
    if platform.system() == "Windows":
        return platform.processor()
    elif platform.system() == "Linux":
        try:
            return subprocess.check_output("cat /proc/cpuinfo | grep 'model name' | uniq", shell=True).decode().split(":")[1].strip()
        except: return "Linux Generic CPU"
    return "Unknown CPU"

# --- 3. FUNGSI BENCHMARK ---
def run_heavy_task(size=8000):
    print(f"\n[WARMUP] Menyiapkan kalkulasi matriks {size}x{size}...")
    start_time = time.time()
    
    # Progress bar simulasi beban kerja
    for _ in tqdm(range(10), desc="Memproses Data di RAM"):
        a = np.random.rand(size, size).astype(np.float32)
        b = np.random.rand(size, size).astype(np.float32)
        np.dot(a, b)
        
    end_time = time.time()
    return round(end_time - start_time, 2)

# --- 4. TAMPILAN DASHBOARD ---
print("="*60)
print(f"       INFITECH CLOUD COMPUTING DEMO - 2026")
print("="*60)
print(f"STATUS LINGKUNGAN : {env_label}")
print(f"OS/PLATFORM       : {platform.system()} {platform.release()}")
print(f"PROCESSOR         : {get_cpu_info()}")
print(f"TOTAL RAM         : {round(psutil.virtual_memory().total / (1024.**3), 2)} GB")

# Cek Akselerasi Hardware (GPU)
gpu_status = "TIDAK TERDETEKSI"
try:
    import torch
    if torch.cuda.is_available():
        gpu_status = f"AKTIF ({torch.cuda.get_device_name(0)})"
except:
    pass
print(f"AKSELERASI GPU    : {gpu_status}")
print("-"*60)

# --- 5. EKSEKUSI & HASIL ---
input("\nTekan ENTER untuk memulai Stress Test...")
durasi = run_heavy_task(8000)

results = [
    ["Parameter", "Hasil Analisis"],
    ["Waktu Eksekusi", f"{durasi} Detik"],
    ["Beban CPU", f"{psutil.cpu_percent()}%"],
    ["Status Suhu", "Meningkat (Lokal) / Stabil (Cloud)"]
]

print("\n" + tabulate(results, headers="firstrow", tablefmt="grid"))

# --- 6. POIN PEMBELAJARAN (KESIMPULAN) ---
print("\n[KESIMPULAN UNTUK MAHASISWA]")
if is_colab:
    print("✅ Kamu menggunakan Resource Pooling milik Google.")
    print("✅ Skalabilitas tinggi: Bisa pindah ke GPU T4/TPU dalam hitungan detik.")
    print("✅ Zero Maintenance: Tidak perlu pusing install library.")
else:
    print("❌ Terbatas pada spesifikasi fisik laptop.")
    print("❌ Menggunakan baterai dan menghasilkan panas pada hardware pribadi.")
    print("❌ Management Overhead: Harus install library secara manual.")
print("="*60)
