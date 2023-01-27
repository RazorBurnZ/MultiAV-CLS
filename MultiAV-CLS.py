import os
import subprocess
import shutil
import zipfile
import requests
import re
import hashlib


ScanDir = ""
base_directory = os.getcwd()
Logs_directory = os.getcwd() + '\Logs'
print('Base working directory : ', base_directory)
print('Get current Logs directory : ', Logs_directory)
while True:
    print("Menu:")
    print("1. Input directory to scan")
    print("2. Update virus definitions")
    print("3. Parse logs")
    print("4. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        ScanDir = input("Enter the directory path: ")
        if os.path.isdir(ScanDir):
            print("The directory exists.")
            if os.path.exists(Logs_directory):
                shutil.rmtree(Logs_directory)
            os.makedirs(Logs_directory)
            
              
            command1 = "Avira\\scancl.exe /a /z --withtype=all --heurlevel=3 --log="+ base_directory + "\Logs\AviraLog.log --logformat=singleline --stats " + ScanDir
            print(command1)
            subprocess.run(command1, shell=True)
            print("Avira scan has been completed.")

            command2 = "McAfee\\scan.exe /HIDEMD5 /FAM /SECURE /PROGRAM /SUB /SHOWCOMP /SHOWENCRYPTED /REPORT=" + base_directory + "\Logs\MCreport.log " + ScanDir
            print(command2)
            subprocess.run(command2, shell=True)
            print("McAfee scan has been completed.")

            command3 = "ClamAV\\clamscan.exe -i -o -r -l " + base_directory + "\Logs\ClamLog.log --detect-pua=yes --remove=no --normalize=no --exclude-pua=Win.Packer " + ScanDir
            print(command3)
            subprocess.run(command3, shell=True)
            print("ClamAV scan has been completed.")
            
            command4 = "EEK\\bin64\\a2cmd.exe /a /am /cloud=1 /pup /la="+ base_directory  + "\Logs\EEK-Report.log " + ScanDir
            print(command4)
            subprocess.run(command4, shell=True)
            print("Emsisoft scan has been completed.")
             
            command5 = "T3scan\\T3Scan_w64.exe -l " + base_directory + "\Logs\Ikarus.log " + ScanDir
            print(command5)
            subprocess.run(command5, shell=True)
            print("IKARUS scan has been completed.")

            command6 = "\"c:\\Program Files\\Windows Defender\\MpCmdRun.exe\" -Scan -ScanType 3 -File " + ScanDir + " -DisableRemediation > " + base_directory + "\Logs\MS-Defender.log"
            print(command6)
            subprocess.run(command6, shell=True)
            print("Microsoft Defender scan has been completed.")

            command7 = "TrendMicro\\vscantm.exe /S /NM /NB /NC /TMAPTN /SSAPTN /LD=" + base_directory + "\Logs\TrendMicro.log /VSSPYWARE+ /LONGVNAME " + ScanDir
            print(command7)
            subprocess.run(command7, shell=True)
            print("TrendMicro scan has been completed.")

            command8 = "RMS\\rms.exe " + ScanDir + " -all -heur -csv -log=" + base_directory + "\Logs\RMS.log -verbose"
            print(command8)
            subprocess.run(command8, shell=True)
            print("RMS scan has been completed.")
            
            
        else:
            print("The directory does not exist.")

    elif choice == "2":
        # Update virus definitions
        
        # Updating Avira Virus definitions
        subprocess.run("Avira/Fusebundle/fusebundle.exe")

        # Unzip vdf_fusebundle.zip to AV\Avira\
        temp_dir = 'Avira/Fusebundle/temp/vdf_fusebundle'
        os.makedirs(temp_dir, exist_ok=True)

        with zipfile.ZipFile("Avira/Fusebundle/install/vdf_fusebundle.zip", "r") as zip_ref:
            zip_ref.extractall(temp_dir)

        for file in os.listdir(temp_dir):
            src_file = os.path.join(temp_dir, file)
            dst_file = os.path.join("Avira/", file)
            shutil.move(src_file, dst_file)
    
        print("Avira virus definitions have been updated.")

        
        # Updating ClamAV Virus definitions
        subprocess.run("ClamAV/freshclam.exe")
        print("ClamAV virus definitions have been updated.")
        
        
        # Updating Comodo Cleaning Essentials Virus definitions
        subprocess.run("CCE/CCE.exe -u")
        print("Comodo Cleaning Essentials virus definitions have been updated.")
       
        # Updating Emsisoft Virus definitions
        subprocess.run("EEK/bin64/a2cmd.exe /u")
        print("Emsisoft virus definitions have been updated.")
             
        # Updating Ikarus Virus definitions
        subprocess.run(["update-ikarus.bat"])
         print("Ikarus virus definitions have been updated.")
         
        # Updating McAfee Virus definitions
        subprocess.run(["update-mcafee.bat"])
        print("McAfee DAT files have been updated.")

        
    elif choice == "3":
        # Parse logs
        subprocess.run("CheckEnc.bat", shell=True)
        subprocess.run("parselogs.py", shell=True)
        print("Parsing Antivirus Scan Logs.")
        pass
        
    elif choice == "4":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")

