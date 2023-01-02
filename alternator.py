from woocommerce import API
from config import *

print(title)

wcapi = API(
    url = url,
    consumer_key = consumer_key,
    consumer_secret = consumer_secret,
    version = "wc/v3"
)
page=1
count=1
per_page=10
while True:
    try:
        print('[+] Page: ' + str(page))
        r = wcapi.get('products', params={'per_page': per_page, 'page': page})
        products = r.json()
        print('[+] Products count: ' + str(len(products)))
        for product in products:
            for img in product['images']:
                payload = {
                    "images":[{
                        'id' : img['id'],
                        'name' : f"{product['name']}-{img['id']}",
                        'alt' : f"{product['categories'][0]['name']} {product['name']} {img['id']}"
                    }]
                }
                print("\nProduct number: "+str(count))
                print(f"[+] ID: {product['id']} \n| Image ID: {str(img['id'])} | ALT: {img['alt']} | ALTERNATED: {product['categories'][0]['name']} {product['name']} {img['id']} | CODE: " + str((wcapi.put(f"products/{product['id']}", payload).status_code)))
                count+=1
    except:
        pass
    page+=1
