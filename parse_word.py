import json

subjects = []
with open("temp_word.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        subject = {}
        try:
            comorbidities = line.strip().split(";")[1].replace("(", "").replace(")", "").split(":")[1].strip().split(",")
        except IndexError:
            comorbidities = []
        pathologies = line.strip().split(";")[0].strip().split("->")
        subject["pathologies"] = [p.strip() for p in pathologies]
        subject["comorbidities"] = [c.strip() for c in comorbidities]
        subjects.append(subject)
with open("temp.json", "w") as json_file:
    json.dump(subjects, json_file, indent=4)