async def Emote_k(uid, emote_id, key, iv, region):
    try:
        url = "https://tcp-emote-api-production-318a.up.railway.app/emote"

        payload = {
            "uid": str(uid),
            "emote": int(emote_id),
            "region": region
        }

        async with aiohttp.ClientSession() as session:
            async with session.post(url, json=payload, timeout=10) as resp:
                if resp.status == 200:
                    data = await resp.json()
                    # API থেকে hex packet আসবে
                    return bytes.fromhex(data["packet"])
                else:
                    print("Emote API error:", resp.status)
                    return None
    except Exception as e:
        print("Emote API failed:", e)
        return None
