import json
from modules.gumroad import upload_products
from modules.bitly import generate_links
from modules.twitter import post_to_twitter
from modules.reddit import post_to_reddit

def main():
    with open('config.json') as f:
        config = json.load(f)

    print("[1/5] Uploading products to Gumroad...")
    product_urls = upload_products(config)

    print("[2/5] Shortening links via Bitly...")
    bitly_links = generate_links(product_urls, config['bitly_token'])

    print("[3/5] Posting Twitter content...")
    post_to_twitter(bitly_links, config['cash_tag'], config['twitter_api'])

    print("[4/5] Posting Reddit content...")
    post_to_reddit(bitly_links, config['cash_tag'], config['reddit'])

    print("✅ Funnel deployed. Monitor sales + scale.")

if __name__ == "__main__":
    main()
