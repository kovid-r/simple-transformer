import json
import argparse

parser = argparse.ArgumentParser(description='Transform customer & order data')
parser.add_argument('--input', help='input JSON filepath')
parser.add_argument('--output', help='output JSON filepath')

args = parser.parse_args()

try: 
    f = open(args.input)
    data = json.load(f)
except Exception as e:
    raise e

customers = []
orders = []

for item in data:
      
    order = {}
    order["id"] = item["id"]
    order["vendor"] = item["vendor"]
    order["date"] = item["date"]
    order["customer"] = item["customer"]["id"]
    customer = item["customer"]
    
    transformed_order_items = []
    order_items = list(item["order"].items())
    for order_item in order_items:
        
        transformed_order_item = {}
        transformed_order_item['item'] = order_item[0]
        transformed_order_item['quantity'] = order_item[1]['quantity']
        transformed_order_item['price'] = order_item[1]['price']
        transformed_order_item['revenue'] = transformed_order_item['quantity'] * transformed_order_item['price']  
        transformed_order_items.append(transformed_order_item)
    
    order["order"] = transformed_order_items
    
    orders.append(order)
    
    if customer not in customers:
        customers.append(customer)

output = {}
output["customers"] = customers
output["orders"] = orders

f.close()

try:
    with open(args.output, 'w') as f:
        json.dump(output, f, ensure_ascii=False, indent=4)
    print(args.input + " successfully converted to " + args.output)
except Exception as e:
    raise e

f.close()
