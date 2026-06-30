import requests
import time

WEBHOOK = "https://discord.com/api/webhooks/1521580456049639578/Sl4nyD2dsHrHXUj8XhW6YgEfN5cauL4jyEnfxEi8Qus0JvVHVTF2CbpQYNoHYn1f3Z_v"

def avisar(group_id):
    url = f"https://www.roblox.com/communities/{group_id}"
    requests.post(WEBHOOK, json={
        "content": f"@everyone nuevo grupo: {url}"
    })

def comprobar(group_id):
    try:
        r = requests.get(f"https://groups.roblox.com/v1/groups/{group_id}")
        if r.status_code != 200:
            return

        data = r.json()

        # Si no tiene owner
        if data.get("owner") is None:
            avisar(group_id)

    except:
        pass

while True:
    for group_id in range(1, 5000):
        comprobar(group_id)
        time.sleep(0.2)
