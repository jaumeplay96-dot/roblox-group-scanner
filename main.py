import requests
from concurrent.futures import ThreadPoolExecutor, as_completed

WEBHOOK = "https://discord.com/api/webhooks/1521580456049639578/Sl4nyD2dsHrHXUj8XhW6YgEfN5cauL4jyEnfxEi8Qus0JvVHVTF2CbpQYNoHYn1f3Z_v"

session = requests.Session()

def enviar(g):
    url = f"https://www.roblox.com/communities/{g['id']}"
    session.post(WEBHOOK, json={
        "content": f"@everyone grupo encontrado:\n{g['name']}\n{url}"
    })

def es_abierto(group_id):
    try:
        url = f"https://groups.roblox.com/v1/groups/{group_id}"
        r = session.get(url, timeout=4)

        if r.status_code != 200:
            return False

        return r.json().get("publicEntryAllowed", False)
    except:
        return False

def procesar_grupo(g):
    group_id = g.get("id")
    if not group_id:
        return

    if es_abierto(group_id):
        enviar(g)

def buscar():
    url = "https://groups.roblox.com/v1/groups/search?keyword=a&limit=10"
    r = session.get(url, timeout=5)

    if r.status_code != 200:
        return

    grupos = r.json().get("data", [])

    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = [executor.submit(procesar_grupo, g) for g in grupos]

        for _ in as_completed(futures):
            pass

buscar()
