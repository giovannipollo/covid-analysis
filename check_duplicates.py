import json

with open("merged_data_final.json", "r") as data_file:
    data = json.load(data_file)

pathologies = []
comorbidities = []
operating_units = []
for i in range(len(data)):
    for j in range(len(data[i]["pathologies"])):
        if data[i]["pathologies"][j] not in pathologies:
            pathologies.append(data[i]["pathologies"][j])
    for j in range(len(data[i]["comorbidities"])):
        if data[i]["comorbidities"][j] not in comorbidities:
            comorbidities.append(data[i]["comorbidities"][j])
        
print("Pathologies:")
for pathology in pathologies:
    print(pathology)
print("\nComorbidities:")
for comorbidity in comorbidities:
    print(comorbidity)