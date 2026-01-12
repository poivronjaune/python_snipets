import subprocess
import json
import time

nw = None
# nw = subprocess.check_output(['netsh', 'wlan', 'show', 'network'])
subprocess.check_output(['netsh', 'wlan', 'disconnect'])
time.sleep(1)
nw = subprocess.check_output(['netsh', 'wlan', 'show', 'networks'])
decoded_nw = nw.decode('ascii')
print(decoded_nw)

networks = []
current = None

for line in decoded_nw.splitlines():
    line = line.strip()

    if line.startswith("SSID"):
        if current:
            networks.append(current)

        ssid = line.split(":", 1)[1].strip()
        current = {
            "ssid": ssid if ssid else None
        }

    elif line.startswith("Network type"):
        current["network_type"] = line.split(":", 1)[1].strip()

    elif line.startswith("Authentication"):
        current["authentication"] = line.split(":", 1)[1].strip()

    elif line.startswith("Encryption"):
        current["encryption"] = line.split(":", 1)[1].strip()

# append last SSID
if current:
    networks.append(current)

print(json.dumps(networks, indent=2))
# Save resulting credentials as a json file
with open(r'saved_ssid.json', 'w') as f:
    json.dump(networks, f, indent=4)     