#!/usr/bin/python3
import re
import json
prod = 0
accuracy = input("Enter search accuracy. Please use a number >= 1. 1 will ONLY display results that match the product 100%: ")
match_chance = 0

try:
    float(accuracy)
except ValueError:
   input("Sorry, that's not a valid input. Please enter a valid input: ")

with open("data/products.txt", "r") as complete_products:
    for products in complete_products:
        prod = prod + 1
        product = json.loads(products)
        search_term = product["product_name"].split("_")
        match_chance = 0
        print("reset")
        print("Product #" + str(prod))
        # with open("test.txt", "r") as complete_listings:
        with open("data/listings.txt", "r") as complete_listings:
            for listings in complete_listings:
                for term in search_term:
                    listing = str(json.loads(listings))
                    search = re.search(term, listing)
                    if search:
                        match_chance = match_chance + 1

                if (match_chance / len(search_term)) >= float(accuracy):
                    print(str(match_chance) + "match")
                    # match_chance = 0
                    with open("data/output.txt", "a") as output:
                        output.write(products)
                        break
