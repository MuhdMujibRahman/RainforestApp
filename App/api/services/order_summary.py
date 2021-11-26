import requests
import json
import pandas as pd


class OrderSummary:
    def __init__(self, request):
        self.income: float = 0.0
        self.profit: float = 0.0
        self.unit_sold : int = 0
        self.order_count : int = 0

    def get_created_orders(self):

        url = "http://127.0.0.1:8000/star-wars/Products/Order"

        payload = {}
        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload)
        return response.text

    def get_summarized_data(self,response):

        df = pd.read_json(response)

        total_quantity = df.groupby(['name'])['quantity'].sum()
        cp = total_quantity.copy()
        newGroupedData = df.groupby(['name']).first()
        for d in range(len(newGroupedData.index)):
            newGroupedData['quantity'][newGroupedData.index[d]] = cp[d]

        newGroupedData['profit'] = newGroupedData['quantity'] * (newGroupedData['price'] - newGroupedData['unit_cost'])
        newGroupedData['income'] = newGroupedData['quantity'] * newGroupedData['price']
        newGroupedData['name'] = newGroupedData.index
        js = newGroupedData.to_json(orient='records')
        return json.loads(js)

