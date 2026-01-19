from product_data import products
from product_data import products

# TODO: Step 1 - Print out the products to see the data that you are working with.
print("Product Catalog Preview:")
for product in products:
    print(product)

# TODO: Step 2 - Create a list called customer_preferences and store the user preference in this list.
customer_preferences = []

response = ""
while response != "N":
    print("Input a preference:")
    preference = input().strip().lower()
    customer_preferences.append(preference)

    response = input("Do you want to add another preference? (Y/N): ").upper()

# TODO: Step 3 - Convert customer_preferences list to set to eliminate duplicates.
customer_preferences_set = set(customer_preferences)

# TODO: Step 4 - Convert the product tags to sets in order to allow for faster comparisons.
converted_products = []

for product in products:
    converted_products.append({
        "name": product["name"],
        "tags": set(product["tags"])
    })

# TODO: Step 5 - Write a function to calculate the number of matching tags
def count_matches(product_tags, customer_tags):
    '''
    Args:
        product_tags (set): A set of tags associated with a product.
        customer_tags (set): A set of tags associated with the customer.
    Returns:
        int: The number of matching tags between the product and customer.
    '''
    return len(product_tags.intersection(customer_tags))

# TODO: Step 6 - Write a function that loops over all products and returns a sorted list of matches
def recommend_products(products, customer_tags):
    '''
    Args:
        products (list): A list of product dictionaries.
        customer_tags (set): A set of tags associated with the customer.
    Returns:
        list: A list of products containing product names and their match counts.
    '''
    recommendations = []

    for product in products:
        match_count = count_matches(product["tags"], customer_tags)
        if match_count > 0:
            recommendations.append({
                "name": product["name"],
                "matches": match_count
            })

    recommendations.sort(key=lambda x: x["matches"], reverse=True)
    return recommendations

# TODO: Step 7 - Call your function and print the results
recommended_products = recommend_products(converted_products, customer_preferences_set)

print("\nRecommended Products:")
for product in recommended_products:
    print(f"- {product['name']} ({product['matches']} match(es))")

# DESIGN MEMO
#1. What data structures did you use and why?
# I primiraly used loops throuhgout my code to iterate over user inputs and the product list.
# I also used sets to store customer preferences and product tags for efficient comparison.
# This allowed me to easily find intersections between customer preferences and product tags.
# This is usually cleaner and faster than nested loops.
#2. How might this code change if you had 1000+ products?
# If the product catalog had 1000+ products, I would consider storing the products in a database
# The core of comparing tags would remain the same, but performance optimizations would be necessary.
# Caching frequent searches or using more advanced data structures could further improve efficiency.