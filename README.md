# MultiAV-CLS: Multiple AntiVirus - Command Line Scanner

MultiAV-CLS is an open-source command line scanner written in python that allows users to scan files and detect malware using multiple antivirus engines. It is designed to be lightweight, fast, portable, and easy to use.

### Features
- Scan one or more files at a time, or an entire directory
- Scan for malware with multiple antivirus engines
- Update virus definitions
- Fully portable
- Ability to parse logs to compare how much malwares was detected by each scanner
- Uses engines from Avira, McAfee, ClamAV, Emsisoft, Ikarus, MS Defender, TrendMicro, and Rose Malware Scanner. Will add more engines in the future
- All engines virus definitions can be updated to the latest version except for TrendMicro and RMS, which I will be updating their update process in future updates for the script


### Requirements:

import os
import subprocess
import shutil
import zipfile
import requests
import re
import hashlib

Follow the directory structure in this sample, or you can modify the script to use your own directory structure
![Image](DirTree.png)
