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
    print("Count checks ...")
    # Check if the number of orders in the input & output are equal
    assert len(data) == len(output["orders"])
    print("\nTest output: Number of orders in the input file: " + str(len(data)) + " are equal to the number of orders in the output file: " + str(len(output["orders"])))
    
    # Check if the number of customers in the input & output are equal
    assert len(collections.Counter(e['customer']['id'] for e in data)) == len(output["customers"]) 
    print("Test output: Number of unique customers in the input file: " + str(len(collections.Counter(e['customer']['id'] for e in data))) + " are equal to the number of unique customers in the output file: " + str(len(output["customers"])))

    # Check if a particular customer exists in the output
    print("\nTesting if customers exist in the output file ...\n")
    for i in range(5):
        random_customer = random.choice(data)["customer"]["id"]
        for customer in output["customers"]:
            if customer["id"] == random_customer:
                print("Test output: Customer with id '" + random_customer + "' is present in the output")

except AssertionError as e:
    raise e
