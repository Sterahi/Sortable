#!/usr/bin/python3
# Using re to do a search through the listings.
import re
import json
prod = 0
with open("data/products.txt", "r") as complete_products:
    for products in complete_products:
        prod = prod + 1
        product = json.loads(products)
        product["product_name"] = product["product_name"].replace("_", " ")
        name_search = product["product_name"]
        print("Product #" + str(prod))
        with open("data/listings.txt", "r") as complete_listings:
            for listings in complete_listings:
                listing = str(json.loads(listings))
                search = re.search(name_search, listing)
                if search:
                    with open("data/output.txt", "a") as output:
                        output.write(products)
