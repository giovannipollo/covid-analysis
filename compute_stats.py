import json
import inspect
from typing import List, Dict


def compute_average_age(data: List[Dict]):
    cumulative_age = 0
    number_of_valid_patients = 0
    for i in range(len(data)):
        birthdate: str = data[i]["birthdate"]
        deathdate: str = data[i]["deathdate"]
        try:
            years_difference: int = int(deathdate.split("-")[0]) - int(
                birthdate.split("-")[0]
            )
            months_difference: float = (
                int(deathdate.split("-")[1]) - int(birthdate.split("-")[1])
            ) / 12
            cumulative_age += abs(years_difference) + abs(months_difference)
            number_of_valid_patients += 1
        except Exception as e:
            func_name = inspect.currentframe().f_code.co_name
            print(
                f"[{func_name}] Exception: {e} | Patient with custom-id {data[i]['custom-id']} has birthdate {data[i]['birthdate']} and deathdate {data[i]['deathdate']}"
            )
    average_age = cumulative_age / number_of_valid_patients
    print("Average age: ", average_age)

def compute_average_age_year(data: List[Dict], year):
    cumulative_age = 0
    number_of_valid_patients = 0
    for i in range(len(data)):
        birthdate: str = data[i]["birthdate"]
        deathdate: str = data[i]["deathdate"]
        if int(deathdate.split("-")[0]) == year:
            try:
                years_difference: int = int(deathdate.split("-")[0]) - int(
                    birthdate.split("-")[0]
                )
                months_difference: float = (
                    int(deathdate.split("-")[1]) - int(birthdate.split("-")[1])
                ) / 12
                cumulative_age += abs(years_difference) + abs(months_difference)
                number_of_valid_patients += 1
            except Exception as e:
                func_name = inspect.currentframe().f_code.co_name
                print(
                    f"[{func_name}] Exception: {e} | Patient with custom-id {data[i]['custom-id']} has birthdate {data[i]['birthdate']} and deathdate {data[i]['deathdate']}"
                )
    average_age = cumulative_age / number_of_valid_patients
    print("Average age for the year ", year, ": ", average_age)


def count_male_female(data: List[Dict]):
    number_of_male: int = 0
    number_of_female: int = 0
    for i in range(len(data)):
        if data[i]["custom-id"] == 13:
            continue
        if data[i]["gender"] == "m":
            number_of_male += 1
        elif data[i]["gender"] == "f":
            number_of_female += 1
        else:
            print("Error in the data")
    print("Number of male: ", number_of_male)
    print("Number of female: ", number_of_female)


def compute_operating_units(data: List[Dict]):
    operating_units = {}
    valid_operating_units = 0
    for i in range(len(data)):
        if data[i]["custom-id"] == 13:
            continue
        valid_operating_units += 1
        if data[i]["operating_unit"] in operating_units:
            operating_units[data[i]["operating_unit"]] += 1
        else:
            operating_units[data[i]["operating_unit"]] = 1
    operating_units = sorted(operating_units.items(), key=lambda x: x[1], reverse=True)
    for operating_unit in operating_units:
        print(
            "{:<15} --> {:>5} --> {:>6.2f}%".format(
                operating_unit[0],
                operating_unit[1],
                round(int(operating_unit[1]) / valid_operating_units * 100, 2),
            )
        )

def compute_comorbidities(data: List[Dict]):
    comorbidities = {}
    number_of_patients_with_comorbidities = 0
    number_of_comorbidities = 0
    for i in range(len(data)):
        if data[i]["custom-id"] == 13:
            continue
        if len(data[i]["comorbidities"]) != 0:
            number_of_patients_with_comorbidities += 1
        for j in range(len(data[i]["comorbidities"])):
            number_of_comorbidities += 1
            if data[i]["comorbidities"][j] in comorbidities:
                comorbidities[data[i]["comorbidities"][j]] += 1
            else:
                comorbidities[data[i]["comorbidities"][j]] = 1
    comorbidities = sorted(comorbidities.items(), key=lambda x: x[1], reverse=True)
    print("Number of patient with comorbidities: ", number_of_patients_with_comorbidities)
    print("------------------------------")
    print("Number of comorbidities: ", number_of_comorbidities)
    print("------------------------------")
    print("Comorbidities")
    for comorbidity in comorbidities:
        print(
            "{:<70} --> {:>5} --> {:>6.2f}%".format(
                comorbidity[0],
                comorbidity[1],
                round(int(comorbidity[1]) / number_of_comorbidities * 100, 2),
            )
        )

def compute_pure_covid(data: List[Dict]):
    patient_with_pure_covid = 0
    for i in range(len(data)):
        if data[i]["custom-id"] == 13:
            continue
        if len(data[i]["pathologies"]) != 0:
            if data[i]["pathologies"][0] == "infezione covid" or data[i]["pathologies"][0] == "polmonite covid":
                patient_with_pure_covid += 1
    print("Numero di pazienti con covid puro: ", patient_with_pure_covid)

def compute_covid_comorbdities(data: List[Dict]):
    patient_with_covid_comorbidities = 0
    for i in range(len(data)):
        if data[i]["custom-id"] == 13:
            continue
        if len(data[i]["comorbidities"]) != 0:
            for j in range(len(data[i]["comorbidities"])):
                if data[i]["comorbidities"][j] == "infezione covid" or data[i]["comorbidities"][j] == "polmonite covid":
                    patient_with_covid_comorbidities += 1
                    break
    print("Numero di pazienti con covid tra le comorbidità: ", patient_with_covid_comorbidities)

def compute_covid_comorbdities(data: List[Dict]):
    patient_with_covid_pathologies = 0
    for i in range(len(data)):
        if data[i]["custom-id"] == 13:
            continue
        if len(data[i]["pathologies"]) > 1:
            for j in range(1, len(data[i]["pathologies"])):
                if data[i]["pathologies"][j] == "infezione covid" or data[i]["pathologies"][j] == "polmonite covid":
                    patient_with_covid_pathologies += 1
                    break
    print("Numero di pazienti con covid tra le patologie: ", patient_with_covid_pathologies)


        

if __name__ == "__main__":
    with open("merged_data_final.json", "r") as data_file:
        data: List[Dict] = json.load(fp=data_file)


    compute_average_age(data=data)
    print("------------------------------")
    count_male_female(data=data)
    print("------------------------------")
    compute_operating_units(data=data)
    print("------------------------------")
    compute_comorbidities(data=data)
    print("------------------------------")
    compute_pure_covid(data=data)
    print("------------------------------")
    compute_covid_comorbdities(data=data)
    print("------------------------------")

