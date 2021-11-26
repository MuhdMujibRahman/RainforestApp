data = [
    {
        "id": 3,
        "payment_status": "paid",
        "order_status": "completed",
        "price": 3.0,
        "unit_cost": 1.5,
        "quantity": 2,
        "name": "Orange Juice",
        "unit_available": 4
    },
    {
        "id": 1,
        "payment_status": "paid",
        "order_status": "completed",
        "price": 3.0,
        "unit_cost": 1.5,
        "quantity": 2,
        "name": "Apple Juice",
        "unit_available": 5
    },
    {
        "id": 2,
        "payment_status": "paid",
        "order_status": "completed",
        "price": 3.0,
        "unit_cost": 1.5,
        "quantity": 2,
        "name": "Apple Juice",
        "unit_available": 4
    }
]

import pandas as pd
import json

df = pd.read_json(json.dumps(data))

total_quantity = df.groupby(['name'])['quantity'].sum()
newGroupedData = df.groupby(['name']).first()
for d in range(len(newGroupedData.index)):
    newGroupedData['quantity'][newGroupedData.index[d]] = total_quantity[d]

newGroupedData['profit'] = newGroupedData['quantity'] * (newGroupedData['price'] - newGroupedData['unit_cost'])
newGroupedData['income'] = newGroupedData['quantity'] * newGroupedData['price']
js = newGroupedData.to_json(orient='records')
print(json.loads(js))
# sortData = df.groupby(['name']).first()
# newDf = sortData[['name', 'unit_cost', 'price']]
# sortData['profit'] = sortData['quantity'] * (sortData['price']-sortData['unit_cost'])
# df = sortData.append(sortData.transpose())
# print(sortData)
