# Simple Transformer

## Project Structure 
 - `requirements.txt` - Use this file to install Python dependencies. Use the following command for installation - `pip3 install -r requirements.txt`
 - `transform.py` - Python script with the transformation logic; takes a JSON file as an input and produces another JSON file
 - `test.py` - Python script to perform some basic sanity checks on the original and transformed data
 - `data.json` - Source data to be transformed (storing data in Git is forbidden; this is only for demonstration purposes)
 - `README.md` - Documentation

## Steps

### Step 1. Install the dependencies from `requirements.txt`

After cloning the repository, run the following command in your terminal window:

```bash
pip install -r requirements.txt
```

### Step 2. Run the transformation using `transform.py`

Run the `transform.py` utility that takes two inputs:

1. The source JSON file that needs to be transformed
2. The destination JSON file path where you want to store the transformed data

```bash
python transform.py --input data.json --output data-transformed.json
```

### Step 3. Run the tests using `test.py`

In this step, you'll perform some basic sanity checks on the transformed data, comparing it with the source data. You'll check:

* if the number of orders in the input & output are equal
* if the number of customers in the input & output are equal
* if a particular customer that exists in the input exists in the output

To perform these tests, run the `test.py` utility that takes the same two inputs as the previous step:

```bash
python test.py --input data.json --output data-transformed.json
```

The output of the tests will be printed on the console.
