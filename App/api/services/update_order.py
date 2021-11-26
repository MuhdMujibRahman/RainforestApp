import requests
import json

class UpdateOrder:
    def __init__(self, request):
        self.name = request.data.get('name')
        self.unti_cost =  request.data.get('unit_cost')
        self.unit_available = (request.data.get('unit_available') - request.data.get('quantity'))
        self.price = request.data.get('price')

    def update_table(self):
        # Making a PUT request

        url = "http://127.0.0.1:8000/star-wars/Products/ByName"

        payload = json.dumps({
            'name': self.name,
            'unit_cost':self.unti_cost,
            'unit_available':self.unit_available,
            'price':self.price
        })
        headers = {
            'Content-Type': 'application/json'
        }

        response = requests.request("PUT", url, headers=headers, data=payload)

        return (response.text)
