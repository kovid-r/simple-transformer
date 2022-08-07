import json
import random
import argparse
import collections

parser = argparse.ArgumentParser(description='Test customer & order data')
parser.add_argument('--input', help='input JSON filepath')
parser.add_argument('--output', help='output JSON filepath')

args = parser.parse_args()

f = open(args.input)
data = json.load(f)
f.close()

f = open(args.output)
output = json.load(f)
f.close()

try:
    print("-> Count checks ...")
    # Check if the number of orders in the input & output are equal
    assert len(data) == len(output["orders"])
    print("\n   Test output: Number of orders in the input file: " + str(len(data)) + " are equal to the number of orders in the output file: " + str(len(output["orders"])))
    
    # Check if the number of customers in the input & output are equal
    assert len(collections.Counter(e['customer']['id'] for e in data)) == len(output["customers"]) 
    print("   Test output: Number of unique customers in the input file: " + str(len(collections.Counter(e['customer']['id'] for e in data))) + " are equal to the number of unique customers in the output file: " + str(len(output["customers"])))

    # Check if a particular customer exists in the output
    print("\n-> Customer checks ...\n   Checking 5 random customers if they exist in the transformed data ...\n")
    random_customers = []
    for i in range(5):
        random_customer = random.choice(data)["customer"]
        random_customers.append(random_customer)
        for customer in output["customers"]:
            if customer["id"] == random_customer["id"]:
                print("   Test output: Customer with id '" + random_customer["id"] + "' is present in the output")
                
    # Check if a particular order exists in the output
    print("\n-> Order checks ...\n   Checking 5 random orders if they exist in the transformed data ...\n")
    random_orders = []
    for i in range(5):
        random_order = random.choice(data)
        random_orders.append(random_order)
        for order in output["orders"]:
            if order["id"] == random_order["id"]:
                print("   Test output: Order with id " + str(random_order["id"]) + " is present in the output")
    
    print("\n--> Checking order details for random order with id " + str(random_order["id"]) + " ...\n")
    for item in data:
        if item["id"] == random_order["id"]:
            input_order = item
            
    for item in output["orders"]:
        if item['id'] == random_order["id"]:
            output_order = item
        
    assert input_order['vendor'] == output_order['vendor']
    assert input_order['date'] == output_order['date']
    assert len(input_order['order']) == len(output_order['order'])
    
    print("    Test output: The vendor, date, and the number of order items is the same in the input and output\n")
    
    input_order_items = []
    for input_order_item in input_order['order']:
        input_order_items.append(input_order_item)
        
    for output_order_item in output_order['order']:
        if output_order_item['item'] == input_order_item:
            print("--> Checking item details for '" + output_order_item['item'] + "' ...\n")
            
            assert input_order['order'][input_order_item]['quantity'] == output_order_item['quantity']
            print("    Test output: The quantity for this order item is correct at " + str(input_order['order'][input_order_item]['quantity']))
            
            assert input_order['order'][input_order_item]['price'] == output_order_item['price']
            print("    Test output: The price for this order item is correct at " + str(input_order['order'][input_order_item]['price']))
            
    print("\nSanity checks completed successfully.")
except AssertionError as e:
    raise e
