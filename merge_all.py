import json


if __name__ == "__main__":
    with open("merged_data.json", "r") as merged_file:
        subjects = json.load(merged_file)
    with open("merged_data_2023.json", "r") as merged_file_2023:
        subjects_2023 = json.load(merged_file_2023)

    subjects_len = len(subjects)
    for i in range(len(subjects_2023)):
        subjects_2023[i]["id"] = i + subjects_len
        subjects_2023[i]["custom-id"] = i + 2
        subjects.append(subjects_2023[i])
    with open("merged_data_final.json", "w") as final_file:
        json.dump(subjects, final_file, indent=4)