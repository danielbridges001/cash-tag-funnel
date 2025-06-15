import requests

def generate_links(urls, token):
    headers = {"Authorization": f"Bearer {token}"}
    short_links = []
    for url in urls:
        res = requests.post(
            "https://api-ssl.bitly.com/v4/shorten",
            json={"long_url": url},
            headers=headers
        )
        data = res.json()
        short_links.append(data.get("link", url))  # fallback to original
    return short_links
