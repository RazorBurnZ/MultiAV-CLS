Echo Updating Ikarus Virus definitions
cd C:\Apps\AV\T3scan\
del t3sigs.vdb.backup
ren C:\Apps\AV\T3scan\t3sigs.vdb t3sigs.vdb.backup
cURL.exe -C - http://updates.ikarus.at/cgi-bin/t3download.pl/t3sigs.vdb -o t3sigs.vdb