
import json
import pathlib
import csv
TESTS_ROOT = (pathlib.Path(__file__).parent).resolve()

filename = TESTS_ROOT / 'test-cad-2020 copy.json'

with open(filename) as f:
    data = json.load(f)
    print(type(data))
    items = []
    for row in data['data']:
        ##print(list(zip(data['fields'], row)))
        item = dict(zip(data['fields'], row))
        items.append(item)

    print(items)
    print(data)

neoFIlename = TESTS_ROOT / 'test-neos-2020 copy.csv'
with open(neoFIlename) as f:
    # Process the CSV file
    reader = csv.DictReader(f)
    for row in reader:
        print(type(row))
        print(row)
    pass