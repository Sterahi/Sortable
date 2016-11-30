#!/usr/bin/python3
# Using re to do a search through the listings.
import re
with open('data/products.txt', 'r') as product:
    for x in product:
        c_product = product.readline().replace('_', ' ')
        p_search = c_product
        with open('data/listings.txt', 'r') as listing:
            for l in listing:
                c_list = str(listing.readline().lower().split('\n'))
                search = re.search(p_search, c_list)
                if search:
                    with open('data/output.txt', 'a') as output:
                        output.write(c_list + '\n',)
