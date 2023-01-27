import re
import os
from prettytable import PrettyTable
import chardet


base_directory = os.getcwd()
Logs_directory = os.path.join(base_directory, 'Logs/')
print('Base working directory : ', base_directory)
print('Get current Logs directory : ', Logs_directory)

# Detect the encoding of the Avira log file
with open(Logs_directory + "AviraLog.log", "rb") as avira_log_file:
    result = chardet.detect(avira_log_file.read())
    avira_encoding = result['encoding']

# Open Avira log file in ASCII encoding
with open(Logs_directory + "AviraLog.log", "rb") as avira_log_file:
    avira_log_text = avira_log_file.read()
    avira_log_text = avira_log_text.decode('ascii', 'ignore')

# Detect the encoding of the ClamAV log file
with open(Logs_directory + "ClamLog.log", "rb") as clamav_log_file:
    result = chardet.detect(clamav_log_file.read())
    clamav_encoding = result['encoding']

# Open ClamAV log file in ASCII encoding
with open(Logs_directory + "ClamLog.log", "rb") as clamav_log_file:
    clamav_log_text = clamav_log_file.read()
    clamav_log_text = clamav_log_text.decode('ascii', 'ignore')

# Detect the encoding of the Emsisoft log file
with open(Logs_directory + "EEK-Report.log", "rb") as emsisoft_log_file:
    result = chardet.detect(emsisoft_log_file.read())
    emsisoft_encoding = result['encoding']

# Open the Emsisoft log file in ASCII encoding
with open(Logs_directory + "EEK-Report.log", "rb") as emsisoft_log_file:
    emsisoft_log_text = emsisoft_log_file.read()
    emsisoft_log_text = emsisoft_log_text.decode('ascii', 'ignore')

# Detect the encoding of the McAfee log file
with open(Logs_directory + "MCreport.log", "rb") as mcafee_log_file:
    result = chardet.detect(mcafee_log_file.read())
    mcafee_encoding = result['encoding']

# Open the McAfee log file in ASCII encoding
with open(Logs_directory + "MCreport.log", "rb") as mcafee_log_file:
    mcafee_log_text = mcafee_log_file.read()
    mcafee_log_text = mcafee_log_text.decode('ascii', 'ignore')

# Detect the encoding of the Ikarus log file
with open(Logs_directory + "Ikarus.log", "rb") as ikarus_log_file:
    result = chardet.detect(ikarus_log_file.read())
    ikarus_encoding = result['encoding']

# Open the Ikarus log file in ASCII encoding
with open(Logs_directory + "Ikarus.log", "rb") as ikarus_log_file:
    ikarus_log_text = ikarus_log_file.read()
    ikarus_log_text = ikarus_log_text.decode('ascii', 'ignore')

with open("c:\\Apps\\AV\\Logs\\MS-Defender.log", "r") as f:
    log_contents = f.read()

# Detect the encoding of the TrendMicro log file
with open(Logs_directory + "TrendMicro.log", "rb") as tm_log_file:
    result = chardet.detect(tm_log_file.read())
    tm_encoding = result['encoding']

# Open the TrendMicro log file in ASCII encoding
with open(Logs_directory + "TrendMicro.log", "rb") as tm_log_file:
    tm_log_text = tm_log_file.read()
    tm_log_text = tm_log_text.decode('ascii', 'ignore')

# Detect the encoding of the RMS log file
with open(Logs_directory + "RMS.log", "rb") as rms_log_file:
    result = chardet.detect(rms_log_file.read())
    rms_encoding = result['encoding']

# Open RMS log file in ASCII encoding
with open(Logs_directory + "RMS.log", "rb") as rms_log_file:
    rms_log_text = rms_log_file.read()
    rms_log_text = rms_log_text.decode('ascii', 'ignore')
    
# Define regular expressions for Avira, ClamAV, Emsisoft, McAfee, Ikarus, and MD logs
avira_pattern = "ALERT: \[(.*)\] (.*) <<< (.*)"
clamav_pattern = "(.*): (.*) FOUND"
emsisoft_pattern = "(.*?)\s+detected: (.*)"
mcafee_pattern = "(.*) ... Found (.*)"
ikarus_pattern = "(.*) - Signature (.*) '(.*)'"
tm_pattern = "(.*) \[(.*)\]"
rms_pattern = "(.*?)\s+Infection:\s+(.*)"


detected_files_avira = set()
detected_files_clamav = set()
detected_files_emsisoft = set()
detected_files_mcafee = set()
detected_files_ikarus = set()
detected_files_tm = set()
detected_files_rms = set()


detected_avira_malware_count = 0
detected_clamav_malware_count = 0
detected_emsisoft_malware_count = 0
detected_mcafee_malware_count = 0
detected_ikarus_malware_count = 0
detected_md_malware_count = 0
detected_tm_malware_count = 0
detected_rms_malware_count = 0

# Check if the log is from Avira

for match in re.finditer(avira_pattern, avira_log_text):
    malware_name = match.group(1)
    file_name = match.group(2)
    file_name = file_name.split(" -->")[0]
    file_name = os.path.basename(file_name)
    if file_name not in detected_files_avira:
        #print("| {:<11} | {:<13} ".format(file_name, malware_name))
        detected_files_avira.add(file_name)
        detected_avira_malware_count += 1


# Check if the log is from ClamAV        

for match in re.finditer(clamav_pattern, clamav_log_text):
    file_name = match.group(1)
    file_name = os.path.basename(file_name)
    malware_name = match.group(2)
    if file_name not in detected_files_clamav:
        #print("| {:<11} | {:<13} ".format(file_name, malware_name))
        detected_files_clamav.add(file_name)
        detected_clamav_malware_count += 1


# Check if the log is from Emsisoft

for match in re.finditer(emsisoft_pattern, emsisoft_log_text):
    file_name = match.group(1)
    file_name = os.path.basename(file_name)
    malware_name = match.group(2)
    if file_name not in detected_files_emsisoft:
        #print("| {:<11} | {:<13} ".format(file_name, malware_name))
        detected_files_emsisoft.add(file_name)
        detected_emsisoft_malware_count += 1


# Check if the log is from Mcafee

for match in re.finditer(mcafee_pattern, mcafee_log_text):
    file_name = match.group(1)
    file_name = os.path.basename(file_name)
    malware_name = match.group(2)
    malware_name = malware_name.replace("the ", "") # Removing "the" from malware name
    if file_name not in detected_files_mcafee:
        #print("| {:<11} | {:<13} ".format(file_name, malware_name))
        detected_files_mcafee.add(file_name)
        detected_mcafee_malware_count += 1


# Check if the log is from Ikarus

for match in re.finditer(ikarus_pattern, ikarus_log_text):
    file_name = match.group(1)
    file_name = os.path.basename(file_name)
    malware_name = match.group(3)
    if file_name not in detected_files_ikarus:
        #print("| {:<11} | {:<13} ".format(file_name, malware_name))
        detected_files_ikarus.add(file_name)
        detected_ikarus_malware_count += 1
        

# Check if the log is from Microsoft Defender

# Search for the threat information in the log contents
for match in re.finditer(r"Threat\s+:\s+(.+)\nResources\s+:\s+\d+\s+total\n((?:\s+file\s+:\s+.+\n)+)", log_contents):
    malware_name = match.group(1)
    files = match.group(2)
    # Split files by newline and remove the "file                : " prefix
    files = [file.split(": ")[1] for file in files.split("\n") if file]
    for file in files:
        file = file.split("->")[0]
        # Get the filename without the path
        file_name = file.split("\\")[-1]
        # Add the file and malware name to the table
        detected_md_malware_count += 1

# Check if the log is from TrendMicro

for match in re.finditer(tm_pattern, tm_log_text):
    file_name = match.group(1)
    file_name = os.path.basename(file_name)
    malware_name = match.group(2)
    if file_name not in detected_files_tm:
        #print("| {:<11} | {:<13} |".format(file_name, malware_name))
        detected_files_tm.add(file_name)
        detected_tm_malware_count += 1        

# Check if the log is from RMS

for match in re.finditer(rms_pattern, rms_log_text):
    file_name = match.group(1)
    file_name = os.path.basename(file_name)
    malware_name = match.group(2)
    if file_name not in detected_files_rms:
        #print("| {:<11} | {:<13} ".format(file_name, malware_name))
        detected_files_rms.add(file_name)
        detected_rms_malware_count += 1
        
        
# Close the log files
avira_log_file.close()
clamav_log_file.close()
emsisoft_log_file.close()
mcafee_log_file.close()
ikarus_log_file.close()
f.close()
tm_log_file.close()
rms_log_file.close()

x = PrettyTable()

x.field_names = ["Antivirus", "Detected Malwares"]
x.add_row(["Avira", detected_avira_malware_count])
x.add_row(["ClamAV", detected_clamav_malware_count])
x.add_row(["Emsisoft", detected_emsisoft_malware_count])
x.add_row(["McAfee", detected_mcafee_malware_count])
x.add_row(["Ikarus", detected_ikarus_malware_count])
x.add_row(["Microsoft Defender", detected_md_malware_count])
x.add_row(["TrendMicro", detected_tm_malware_count])
x.add_row(["RMS", detected_rms_malware_count])

print(x)