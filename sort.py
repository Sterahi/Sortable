from collections import defaultdict
import json  # Import JSON to handle read/write of json objects.
with open("data/products.txt", "r") as complete_products:
    prod = 0  # Declaring global counter
    for products in complete_products:
        # Global declaration to prevent it being recreated
        data = defaultdict(list)
        #  list_complete initialized and set to null.
        list_complete = []
        # Used as a counter to show progress
        prod = prod + 1
        print("Product #" + str(prod))  # Printing to track progress
        product = json.loads(products)  # Loading JSON to Dict
        # Normalizing the input for searching.
        search_product = product["product_name"].replace("_", " ")
        # Opening the listings
        with open("data/listings.txt", "r") as complete_listings:
            for listings in complete_listings:
                listing = json.loads(listings)
                if search_product in listing["title"]:
                    list_complete.append(listing)

        # Called at the end of each product. Only if entry exists.
        if len(list_complete) >= 1:
            # Write to the text file
            with open("data/output.txt", "a") as output:
                data["product_name"] = product["product_name"]
                # Writing complete list to file to avoid unhashable errors.
                data["listings"] = list_complete
                json.dump(data, output)
                output.write(" " + "\n")  # Writing new line.
