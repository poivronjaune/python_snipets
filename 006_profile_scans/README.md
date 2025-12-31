# Network tools  

netsh.exe is a tool for PC users that helps check networl configurations. It gives access to saved wifi profiles and passwords and can be extracted easily with a few lines of python code.  
  
This script lists the PC's saved profiles, then loops through each one to get the passwords in clear.  

### Command line 
```
netsh.exe wlan show profiles
```

Display output
```
Profiles on interface Wi-Fi:

Group policy profiles (read only)
---------------------------------
    <None>

User profiles
-------------
    All User Profile     : Lab
    All User Profile     : Delta_GUEST
    All User Profile     : mywifi
``` 

Then using one of the Profile Names, list the password:
```
netsh.exe wlan show profile "Lab" key=clear
```

Password will be displayed in clear in the fiels "Key Content", see below
```
Profile Lab on interface Wi-Fi:
=======================================================================

Applied: All User Profile    

Profile information
-------------------
    Version                : 1
    Type                   : Wireless LAN
    Name                   : Lab
    Control options        :
        Connection mode    : Connect manually
        Network broadcast  : Connect only if this network is broadcasting
        AutoSwitch         : Do not switch to other networks
        MAC Randomization  : Disabled

Connectivity settings
---------------------
    Number of SSIDs        : 1
    SSID name              : "Lab"
    Network type           : Infrastructure
    Radio type             : [ Any Radio Type ]
    Vendor extension          : Not present

Security settings
-----------------
    Authentication         : WPA3-Personal
    Cipher                 : GCMP-256
    Authentication         : WPA3-Personal
    Cipher                 : GCMP
    Authentication         : WPA3-Personal
    Cipher                 : CCMP
    Authentication         : WPA2-Personal
    Cipher                 : GCMP
    Authentication         : WPA2-Personal
    Cipher                 : CCMP
    Security key           : Present
    Key Content            : password_in_clear_text

Cost settings
-------------
    Cost                   : Unrestricted
    Congested              : No
    Approaching Data Limit : No
    Over Data Limit        : No
    Roaming                : No
    Cost Source            : Default