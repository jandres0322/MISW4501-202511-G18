import requests
import os

def get_product_info(id):
    response = requests.get(f"{os.getenv('PRODUCT_SERVICE_URL')}/products/{id}")
    if response.status_code == 200:
        return response.json()
    return None