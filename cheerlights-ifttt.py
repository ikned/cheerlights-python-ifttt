import requests
import time

while True:
    try:
        r = requests.get('http://api.thingspeak.com/channels/1417/field/2/last.json')
        cheerlights = r.json()
        cheercolor = cheerlights['field2']
        payload = { "value1" : cheercolor }
        
# create your webhook in IFTTT and add it to the next line
        p = http://requests.post('https://maker.ifttt.com/trigger/cheerlights_color/with/key/yourapikeygoeshere', data=payload)
        print (p.text)
    except (ValueError, RuntimeError) as e:
        print("Some error occured, retrying! -", e)

    time.sleep(60)
