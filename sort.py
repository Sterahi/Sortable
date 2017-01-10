import re  # Using re to do a search through the listings.
import json  # Import JSON to handle read/write of json objects.
prod = 0
data = {}  # Global declaration to prevent it being recreated
with open("data/products.txt", "r") as complete_products:
    for products in complete_products:
        prod = prod + 1  # Used as a counter to show progress
        print("Product #" + str(prod))
        product = json.loads(products)  # Loading JSON to Dict
        # Normalizing the input for searching.
        product["product_name"] = product["product_name"].replace("_", " ")
        # Opening the listings
        with open("data/listings.txt", "r") as complete_listings:
            for listings in complete_listings:
                listing = json.loads(listings)
                with open("data/output.json", "a") as output:
                    if product["product_name"] in str(listing):
                        listing["product"] = product["product_name"]
                        json.dump(listing, output)
                        # print(data)
                        # output.write(json.dumps + "\n")
                        # json.dump(listing, output)

                # data2 = {"people": [{"n": "d", "w": "as", "f": "nb"}]}
                # with open("data/output.json", "a") as output:
                #     json.dump(data, output)
                #     data = None
