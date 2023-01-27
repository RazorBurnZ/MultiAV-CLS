import os
import requests
import io
import hashlib
from concurrent.futures import ThreadPoolExecutor
from tqdm import tqdm
from datetime import datetime

MIRROR_SITES = [ "http://rose-swe.bplaced.net/dl", "https://rose.rult.at/dl", "https://www.sac.sk/download/avir"]
subfolder = "Zip"

print("ROSE SWE automatic updater for Linux or Win32/cygwin using python requests and io module")

response = requests.get(f"{MIRROR_SITES[0]}/md5sums.md5")
response.raise_for_status()
with io.open("md5sums.md5", "w", newline='', encoding='utf-8') as f:
    f.write(response.text)

programs = ["rhbvs", "rms", "MemScan", "MPScan"]

if not os.path.exists(subfolder):
    os.mkdir(subfolder)

def download_file(file_url, file_name, mirror_site):
    start_time = datetime.now()
    response = requests.get(file_url, stream=True)
    response.raise_for_status()
    total_size = int(response.headers.get("Content-Length", 0))
    block_size = 8192
    progress_bar = tqdm(total=total_size, unit='B', unit_scale=True, desc=f"{file_name} from {mirror_site}", ascii=True)
    with open(os.path.join(subfolder, file_name), "wb") as f:
        for data in response.iter_content(block_size):
            f.write(data)
            progress_bar.update(len(data))
    progress_bar.close()
    with open(os.path.join(subfolder, file_name), "rb") as f:
        content = f.read()
        m = hashlib.md5()
        m.update(content)
        if m.hexdigest() == expected_md5:
            print(f"[OK] {file_name}: No newer version available!")
        else:
            os.remove(os.path.join(subfolder, file_name))
            download_file(file_url, file_name, mirror_site)
    end_time = datetime.now()
    print(f"[INFO] Download time from {mirror_site} : {end_time - start_time}")

with io.open("md5sums.md5", newline='', encoding='utf-8') as f:
    files = [(f"{MIRROR_SITES[0]}/{line.split()[1]}", line.split()[1], line.split()[0]) for line in f.readlines() if any(i in line for i in programs)]

with ThreadPoolExecutor() as executor:
    for file_url, file_name, expected_md5 in files:
        if not os.path.isfile(os.path.join(subfolder,file_name)):
            for mirror_site in MIRROR_SITES:
                try:
                    response = requests.head(f"{mirror_site}/{file_name}")
                    if response.status_code == 200:
                        file_url = f"{mirror_site}/{file_name}"
                        break
                except:
                    pass
            executor.submit(download_file, file_url, file_name, mirror_site)
            print(f"[!!] {file_name}: Trying to download new/updated file")
        else:
            with open(os.path.join(subfolder,file_name), "rb") as f:
                content = f.read()
                m = hashlib.md5()
                m.update(content)
            if m.hexdigest() == expected_md5:
                print(f"[OK] {file_name}: No newer version available!")
            else:
                os.remove(os.path.join(subfolder, file_name))
                for mirror_site in MIRROR_SITES:
                    try:
                        response = requests.head(f"{mirror_site}/{file_name}")
                        if response.status_code == 200:
                            file_url = f"{mirror_site}/{file_name}"
                            break
                    except:
                        pass
                executor.submit(download_file, file_url, file_name, mirror_site)
                print(f"[!!] {file_name}: Corrupted file, Redownloading...")


exit(0)

