import requests

WEBHOOK = "https://discord.com/api/webhooks/1521580456049639578/Sl4nyD2dsHrHXUj8XhW6YgEfN5cauL4jyEnfxEi8Qus0JvVHVTF2CbpQYNoHYn1f3Z_v"

def enviar(g):
    url = f"https://www.roblox.com/communities/{g['id']}"
    requests.post(WEBHOOK, json={
        "content": f"@everyone grupo encontrado:\n{g['name']}\n{url}"
    })

def buscar():
    url = "https://groups.roblox.com/v1/groups/search?keyword=a&limit=10"

    r = requests.get(url)
    if r.status_code != 200:
        return

    data = r.json().get("data", [])

    for g in data:
        if not g.get("name"):
            continue

        if g.get("owner") is None:
            enviar(g)

buscar()
