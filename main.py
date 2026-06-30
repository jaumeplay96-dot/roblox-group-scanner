import requests
import time

WEBHOOK = "https://discord.com/api/webhooks/1521580456049639578/Sl4nyD2dsHrHXUj8XhW6YgEfN5cauL4jyEnfxEi8Qus0JvVHVTF2CbpQYNoHYn1f3Z_v"

enviados = set()

def enviar(data):
    url = f"https://www.roblox.com/communities/{data['id']}"

    requests.post(WEBHOOK, json={
        "content": f"@everyone posible grupo interesante:\n"
                   f"Nombre: {data['name']}\n"
                   f"{url}"
    })

def comprobar(group_id):
    try:
        r = requests.get(f"https://groups.roblox.com/v1/groups/{group_id}")

        if r.status_code != 200:
            return

        data = r.json()

        group_id = data.get("id")

        # ❌ evitar duplicados
        if group_id in enviados:
            return

        # ❌ tiene owner = no interesa
        if data.get("owner") is not None:
            return

        # ❌ si no es público
        if not data.get("publicEntryAllowed", False):
            return

        # ❌ si no tiene nombre válido
        if not data.get("name"):
            return

        enviados.add(group_id)

        enviar({
            "id": group_id,
            "name": data["name"]
        })

    except:
        pass


while True:
    for group_id in range(1, 30000):
        comprobar(group_id)
        time.sleep(0.1)
