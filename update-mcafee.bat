Echo Updating McAfee DAT files

:1 Download gdeltaavv.ini
    echo  cURL.exe http://update.nai.com/products/commonupdater/gdeltaavv.ini -o McAfee\DATS\gdeltaavv.ini
    cURL.exe http://update.nai.com/products/commonupdater/gdeltaavv.ini -o McAfee\DATS\gdeltaavv.ini
    echo.

:2 Parse gdeltaavv.ini
    for /F "usebackq skip=2 delims== tokens=1,2*" %%m in (`Find /I "CurrentVersion" McAfee\DATS\gdeltaavv.ini`) do set Curr=%%n
    echo  CurrentVersion=%Curr%
    echo.

:3 Download current avvdat zip
    echo  cURL.exe -C - http://update.nai.com/products/commonupdater/avvdat-%Curr%.zip -o McAfee\DATS\avvdat-%Curr%.zip
    cURL.exe -C - http://update.nai.com/products/commonupdater/avvdat-%Curr%.zip -o McAfee\DATS\avvdat-%Curr%.zip

:4 Extract to McAfee dir
sfk.exe unzip McAfee\DATS\avvdat-%Curr%.zip -yes -todir AV\McAfee\
