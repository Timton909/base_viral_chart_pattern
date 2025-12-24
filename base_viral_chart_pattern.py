import requests, time

def viral_pattern():
    print("Base — Viral Chart Pattern (flat → +300% in 3 min)")
    history = {}  # addr → (time, price)

    while True:
        try:
            r = requests.get("https://api.dexscreener.com/latest/dex/pairs/base")
            now = time.time()

            for pair in r.json().get("pairs", []):
                addr = pair["pairAddress"]
                price = float(pair.get("priceUsd", 0))
                change_5m = pair.get("priceChange", {}).get("m5", 0)
                age = now - pair.get("pairCreatedAt", 0) / 1000

                if age > 900 or age < 180: continue

                if addr not in history:
                    history[addr] = (now, price)
                    continue

                last_t, last_p = history[addr]
                if now - last_t > 180: 
                    history[addr] = (now, price)
                    continue

                if abs(change_5m) > 300 and price > last_p * 3:
                    token = pair["baseToken"]["symbol"]
                    print(f"VIRAL PATTERN HIT\n"
                          f"{token} +{change_5m:.0f}% in 5 min\n"
                          f"Price ×3 from base\n"
                          f"https://dexscreener.com/base/{addr}\n"
                          f"→ Classic moonshot breakout\n"
                          f"{'VIRAL'*30}")
                    del history[addr]

                history[addr] = (now, price)

        except:
            pass
        time.sleep(5.4)

if __name__ == "__main__":
    viral_pattern()
