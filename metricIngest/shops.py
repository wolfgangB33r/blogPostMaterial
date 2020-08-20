"""
Example script
"""
import requests, time, sched, random, datetime

YOUR_DT_API_URL = 'YOUR_URL'
YOUR_DT_API_TOKEN = 'YOUR_SECRET'

METRICS = [
    {'id' : 'business.shop.revenue', 'dims' : {'country' : 'us', 'region' : 'useast', 'city' : 'Charlotte', 'store' : 'shop1'}, 'min' : 10, 'max' : 80 },
    {'id' : 'business.shop.revenue', 'dims' : {'country' : 'us', 'region' : 'useast', 'city' : 'Jacksonville', 'store' : 'shop2'}, 'min' : 5, 'max' : 90 },
    {'id' : 'business.shop.revenue', 'dims' : {'country' : 'us', 'region' : 'useast', 'city' : 'Indianapolis', 'store' : 'shop3'}, 'min' : 15, 'max' : 94 },
    {'id' : 'business.shop.revenue', 'dims' : {'country' : 'us', 'region' : 'useast', 'city' : 'Columbus', 'store' : 'shop4'}, 'min' : 20, 'max' : 70 },
    {'id' : 'business.shop.revenue', 'dims' : {'country' : 'us', 'region' : 'useast', 'city' : 'NewYork', 'store' : 'shop5'}, 'min' : 40, 'max' : 90 },
    {'id' : 'business.shop.revenue', 'dims' : {'country' : 'us', 'region' : 'uswest', 'city' : 'SanFrancisco', 'store' : 'shop6'}, 'min' : 80, 'max' : 120 },
    {'id' : 'business.shop.revenue', 'dims' : {'country' : 'us', 'region' : 'uswest', 'city' : 'Seatle', 'store' : 'shop7'}, 'min' : 70, 'max' : 130 },
    {'id' : 'business.shop.revenue', 'dims' : {'country' : 'us', 'region' : 'uswest', 'city' : 'SanDiego', 'store' : 'shop8'}, 'min' : 90, 'max' : 140 },
    {'id' : 'business.shop.revenue', 'dims' : {'country' : 'us', 'region' : 'uswest', 'city' : 'Portland', 'store' : 'shop9'}, 'min' : 77, 'max' : 150 },
    {'id' : 'business.shop.revenue', 'dims' : {'country' : 'us', 'region' : 'uswest', 'city' : 'Anaheim', 'store' : 'shop10'}, 'min' : 90, 'max' : 120 }
]

scheduler = sched.scheduler(time.time, time.sleep)

def genSeries():
    mStr = ""
    for metric in METRICS:
        dimStr = ""
        for dK in metric['dims']:
            dimStr += "," + dK + "=" + metric['dims'][dK]
        mStr += metric['id'] + dimStr + " " + str(random.randint(metric['min'], metric['max'])) + "\n"
    return mStr


def doit():
    scheduler.enter(60, 1, doit)
    payload = genSeries()
    print(payload)
    r = requests.post(YOUR_DT_API_URL + '/api/v2/metrics/ingest', headers={'Content-Type': 'text/plain', 'Authorization' : 'Api-Token ' + YOUR_DT_API_TOKEN}, data=payload)
    print(r)
    print(r.text)

print("START")
scheduler.enter(1, 1, doit)
scheduler.run()
