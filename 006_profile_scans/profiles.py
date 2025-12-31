import subprocess
import json

nw = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles'])
decoded_nw = nw.decode('ascii')

# Extract saved user profiles from PC
profiles = []
for line in decoded_nw.splitlines():
    if "All User Profile" in line:
        profile_name = line.split(":", 1)[1].strip()
        profiles.append(profile_name)

# Get passwords in clear for each profile
credentials = []
for profile in profiles:
    details = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', profile, 'key=clear'])
    decoded_details = details.decode('ascii')
    for line in decoded_details.splitlines():
        if "Key Content" in line:
            password = line.split(":", 1)[1].strip()
            credentials.append({'ssid': profile, 'pw': password})
            print(f"Profile: {profile}, Password: {password}")  

# Save resulting credentials as a json file
with open(r'saved_pw.json', 'w') as f:
    json.dump(credentials, f, indent=4) 
print("Credentials saved to wifi_credentials.json")

