import requests

def upload_products(config):
    api_key = config["gumroad_api_key"]
    uploaded = []
    for product in config["products"]:
        res = requests.post("https://api.gumroad.com/v2/products", data={
            "access_token": api_key,
            "name": product["title"],
            "description": product["description"],
            "price": product["price"] * 100  # cents
        })
        data = res.json()
        try:
            short_url = data['product']['short_url']
            uploaded.append(short_url)
        except:
            print("Upload failed or product already exists.")
    return uploaded
