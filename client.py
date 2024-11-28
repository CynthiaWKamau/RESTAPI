import requests

BASE_URL = "http://127.0.0.1:8000/products/"

# Add a new product
def create_product(name, description, price):
    data = {
        "name": name,
        "description": description,
        "price": price
    }
    response = requests.post(BASE_URL, json=data)
    print("Response:", response.status_code, response.json())

# Get all products
def get_products():
    response = requests.get(BASE_URL)
    print("Response:", response.status_code, response.json())

# Example usage
if __name__ == "__main__":
    # Add a product
    create_product("Cleanser", "Sunscreen", 1500.0)

    # Fetch all products
    get_products()
