import json

with open("merged_data_final.json") as data_file:
    data_alice = json.load(data_file)

for line in data_alice:
    if line["pathologies"][-1] != line["cause-of-death"]:
        print("Error in id: ", line["id"])