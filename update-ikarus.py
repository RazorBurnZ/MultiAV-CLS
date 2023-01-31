import requests
import re
import hashlib
from prettytable import PrettyTable

url = "http://updates.ikarus.at/updates/update.html"
response = requests.get(url)

# File paths for local files
t3sigs_path = r"T3scan\t3sigs.vdb"
t3scan_path = r"T3scan\ikarust3scan.exe"
t3scan_w64_path = r"T3scan\ikarust3scan_w64.exe"

# List of local files and their corresponding online hash value and download url
files = [
    (t3sigs_path, re.search(r'<tr class="grey"><td>T3 VDB</td><td>.*</td><td>.*</td><td>&nbsp;(\w+)</td>', response.text).group(1), "http://updates.ikarus.at/cgi-bin/t3download.pl/t3sigs.vdb"),
    (t3scan_path, re.search(r'<tr class="grey"><td>T3 Commandline<br />Scanner</td><td>.*</td><td>.*</td><td>&nbsp;(\w+)</td>', response.text).group(1), "http://updates.ikarus.at/cgi-bin/t3download.pl/ikarust3scan.exe"),
    (t3scan_w64_path, re.search(r'<tr class="grey"><td>T3 Commandline<br />Scanner \(64bit\)</td><td>.*</td><td>.*</td><td>&nbsp;(\w+)</td>', response.text).group(1), "http://updates.ikarus.at/cgi-bin/t3download.pl/ikarust3scan_w64.exe")
]

table = PrettyTable(["File", "Local MD5", "Remote MD5", "Updated?"])
table.align = 'l'

for file_path, online_hash, download_url in files:
    with open(file_path, "rb") as f:
        content = f.read()
    local_hash = hashlib.md5(content).hexdigest()
    updated = "Yes" if local_hash == online_hash else "No"
    table.add_row([file_path, local_hash, online_hash, updated])

print(table)
os.remove("update.html")

for file_path, online_hash, download_url in files:
    with open(file_path, "rb") as f:
        content = f.read()
    local_hash = hashlib.md5(content).hexdigest()
    if local_hash == online_hash:
        continue
    else:
        download = input(f"Do you want to download the latest update for {file_path}? [Y/n]")
        if download.lower() in ["yes", "y"]:
            response = requests.get(download_url)
            with open(file_path, "wb") as f:
                f.write(response.content)
            print(f"{file_path} has been updated.")
        else:
            continue
