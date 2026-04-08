import time
import urllib.request
import os

def get_http_latency(url):
    try:
        start = time.time()
        # Mengambil header saja (lebih cepat) untuk ngetes respon
        response = urllib.request.urlopen(url, timeout=5)
        end = time.time()
        return round((end - start) * 1000, 2)
    except Exception as e:
        return None

# Daftar Target (Gunakan HTTPS agar valid)
targets = {
    "UNP (Lokal Padang)": "https://unp.ac.id",
    "Google (Global/Asia)": "https://www.google.com",
    "GitHub (USA)": "https://github.com",
    "BBC (Eropa)": "https://www.bbc.com"
}

env = "☁️ CLOUD (Colab)" if 'COLAB_RELEASE_TAG' in os.environ else "💻 LOCAL (Laptop)"
print(f"--- TESTING HTTP LATENCY ON {env} ---")
print(f"{'Target Server':<25} | {'Latency (ms)':<15}")
print("-" * 45)

for name, url in targets.items():
    latency = get_http_latency(url)
    status = f"{latency} ms" if latency else "Timeout/Gagal"
    print(f"{name:<25} | {status:<15}")

print("-" * 45)
