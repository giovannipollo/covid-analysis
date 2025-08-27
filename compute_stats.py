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
        if data[i]["gender"] == "m":
            number_of_male += 1
        elif data[i]["gender"] == "f":
            number_of_female += 1
        else:
            print("Error in the data")
    print("Number of male: ", number_of_male)
    print("Number of female: ", number_of_female)


def count_male_female_year(data: List[Dict], year):
    number_of_male: int = 0
    number_of_female: int = 0
    for i in range(len(data)):
        deathdate: str = data[i]["deathdate"]
        if int(deathdate.split("-")[0]) == year:
            if data[i]["gender"] == "m":
                number_of_male += 1
            elif data[i]["gender"] == "f":
                number_of_female += 1
            else:
                print("Error in the data")
    print("Number of male for year ", year, ": ", number_of_male)
    print("Number of female for year ", year, ": ", number_of_female)


def compute_operating_units(data: List[Dict]):
    operating_units = {}
    valid_operating_units = 0
    for i in range(len(data)):
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


def compute_operating_units_year(data: List[Dict], year):
    operating_units = {}
    valid_operating_units = 0
    for i in range(len(data)):
        deathdate: str = data[i]["deathdate"]
        if int(deathdate.split("-")[0]) == year:
            valid_operating_units += 1
            if data[i]["operating_unit"] in operating_units:
                operating_units[data[i]["operating_unit"]] += 1
            else:
                operating_units[data[i]["operating_unit"]] = 1

    operating_units = sorted(operating_units.items(), key=lambda x: x[1], reverse=True)
    print("Operating units for the year ", year)
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
        if len(data[i]["comorbidities"]) != 0:
            number_of_patients_with_comorbidities += 1
        for j in range(len(data[i]["comorbidities"])):
            number_of_comorbidities += 1
            if data[i]["comorbidities"][j] in comorbidities:
                comorbidities[data[i]["comorbidities"][j]] += 1
            else:
                comorbidities[data[i]["comorbidities"][j]] = 1
    comorbidities = sorted(comorbidities.items(), key=lambda x: x[1], reverse=True)
    print(
        "Number of patient with comorbidities: ", number_of_patients_with_comorbidities
    )
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


def compute_comorbidities_year(data: List[Dict], year):
    comorbidities = {}
    number_of_patients_with_comorbidities = 0
    number_of_comorbidities = 0
    for i in range(len(data)):
        deathdate: str = data[i]["deathdate"]
        if int(deathdate.split("-")[0]) == year:
            if len(data[i]["comorbidities"]) != 0:
                number_of_patients_with_comorbidities += 1
            for j in range(len(data[i]["comorbidities"])):
                number_of_comorbidities += 1
                if data[i]["comorbidities"][j] in comorbidities:
                    comorbidities[data[i]["comorbidities"][j]] += 1
                else:
                    comorbidities[data[i]["comorbidities"][j]] = 1
    comorbidities = sorted(comorbidities.items(), key=lambda x: x[1], reverse=True)
    print(
        "Number of patient with comorbidities for the year ",
        year,
        ": ",
        number_of_patients_with_comorbidities,
    )
    print("------------------------------")
    print("Number of comorbidities for the year ", year, ": ", number_of_comorbidities)
    print("------------------------------")
    print("Comorbidities for the year ", year)
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
        if len(data[i]["pathologies"]) != 0:
            if (
                data[i]["pathologies"][0] == "infezione covid"
                or data[i]["pathologies"][0] == "polmonite covid"
            ):
                patient_with_pure_covid += 1
    print("Numero di pazienti con covid puro: ", patient_with_pure_covid)


def compute_pure_covid_year(data: List[Dict], year):
    patient_with_pure_covid = 0
    for i in range(len(data)):
        deathdate: str = data[i]["deathdate"]
        if int(deathdate.split("-")[0]) == year:
            if len(data[i]["pathologies"]) != 0:
                if (
                    data[i]["pathologies"][0] == "infezione covid"
                    or data[i]["pathologies"][0] == "polmonite covid"
                ):
                    patient_with_pure_covid += 1
    print(
        "Numero di pazienti con covid puro per l'anno ",
        year,
        ": ",
        patient_with_pure_covid,
    )


def compute_pure_covid_no_comorbidities(data: List[Dict]):
    patient_with_pure_covid_no_comorbidities = 0
    for i in range(len(data)):
        if len(data[i]["pathologies"]) != 0 and len(data[i]["comorbidities"]) == 0:
            if (
                data[i]["pathologies"][0] == "infezione covid"
                or data[i]["pathologies"][0] == "polmonite covid"
            ):
                patient_with_pure_covid_no_comorbidities += 1
    print(
        "Numero di pazienti con covid puro senza comorbidità: ",
        patient_with_pure_covid_no_comorbidities,
    )


def compute_pure_covid_no_comorbidities_year(data: List[Dict], year):
    patient_with_pure_covid_no_comorbidities = 0
    for i in range(len(data)):
        deathdate: str = data[i]["deathdate"]
        if int(deathdate.split("-")[0]) == year:
            if len(data[i]["pathologies"]) != 0 and len(data[i]["comorbidities"]) == 0:
                if (
                    data[i]["pathologies"][0] == "infezione covid"
                    or data[i]["pathologies"][0] == "polmonite covid"
                ):
                    patient_with_pure_covid_no_comorbidities += 1
    print(
        "Numero di pazienti con covid puro senza comorbidità per l'anno ",
        year,
        ": ",
        patient_with_pure_covid_no_comorbidities,
    )


def compute_pure_covid_with_comorbidities(data: List[Dict]):
    patient_with_pure_covid_with_comorbidities = 0
    for i in range(len(data)):
        if len(data[i]["pathologies"]) != 0 and len(data[i]["comorbidities"]) != 0:
            if (
                data[i]["pathologies"][0] == "infezione covid"
                or data[i]["pathologies"][0] == "polmonite covid"
            ):
                patient_with_pure_covid_with_comorbidities += 1
    print(
        "Numero di pazienti con covid puro con almeno una comorbidità: ",
        patient_with_pure_covid_with_comorbidities,
    )


def compute_pure_covid_with_comorbidities_year(data: List[Dict], year):
    patient_with_pure_covid_with_comorbidities = 0
    for i in range(len(data)):
        deathdate: str = data[i]["deathdate"]
        if int(deathdate.split("-")[0]) == year:
            if len(data[i]["pathologies"]) != 0 and len(data[i]["comorbidities"]) != 0:
                if (
                    data[i]["pathologies"][0] == "infezione covid"
                    or data[i]["pathologies"][0] == "polmonite covid"
                ):
                    patient_with_pure_covid_with_comorbidities += 1
    print(
        "Numero di pazienti con covid puro con almeno una comorbidità per l'anno ",
        year,
        ": ",
        patient_with_pure_covid_with_comorbidities,
    )


def compute_covid_comorbdities(data: List[Dict]):
    patient_with_covid_comorbidities = 0
    for i in range(len(data)):
        if len(data[i]["comorbidities"]) != 0:
            for j in range(len(data[i]["comorbidities"])):
                if (
                    data[i]["comorbidities"][j] == "infezione covid"
                    or data[i]["comorbidities"][j] == "polmonite covid"
                ):
                    patient_with_covid_comorbidities += 1
                    break
    print(
        "Numero di pazienti con covid tra le comorbidità: ",
        patient_with_covid_comorbidities,
    )


def compute_covid_comorbdities_year(data: List[Dict], year):
    patient_with_covid_comorbidities = 0
    for i in range(len(data)):
        deathdate: str = data[i]["deathdate"]
        if int(deathdate.split("-")[0]) == year:
            if len(data[i]["comorbidities"]) != 0:
                for j in range(len(data[i]["comorbidities"])):
                    if (
                        data[i]["comorbidities"][j] == "infezione covid"
                        or data[i]["comorbidities"][j] == "polmonite covid"
                    ):
                        patient_with_covid_comorbidities += 1
                        break
    print(
        "Numero di pazienti con covid tra le comorbidità nell'anno ",
        year,
        ": ",
        patient_with_covid_comorbidities,
    )


def compute_covid_pathologies(data: List[Dict]):
    patient_with_covid_pathologies = 0
    for i in range(len(data)):
        if len(data[i]["pathologies"]) > 1:
            for j in range(1, len(data[i]["pathologies"])):
                if (
                    data[i]["pathologies"][j] == "infezione covid"
                    or data[i]["pathologies"][j] == "polmonite covid"
                ):
                    patient_with_covid_pathologies += 1
                    break
    print(
        "Numero di pazienti con covid tra le patologie: ",
        patient_with_covid_pathologies,
    )


def compute_covid_pathologies_year(data: List[Dict], year):
    patient_with_covid_pathologies = 0
    for i in range(len(data)):
        deathdate: str = data[i]["deathdate"]
        if int(deathdate.split("-")[0]) == year:
            if len(data[i]["pathologies"]) > 1:
                for j in range(1, len(data[i]["pathologies"])):
                    if (
                        data[i]["pathologies"][j] == "infezione covid"
                        or data[i]["pathologies"][j] == "polmonite covid"
                    ):
                        patient_with_covid_pathologies += 1
                        break
    print(
        "Numero di pazienti con covid tra le patologie nell'anno ",
        year,
        ": ",
        patient_with_covid_pathologies,
    )


def compute_comorbidities_groups(data: List[Dict], groups: List[Dict]):
    groups_occurence = {
        "cardiovascular": 0,
        "respiratory": 0,
        "metabolic": 0,
        "neurodegenerative-neocognitive": 0,
        "neoplastic": 0,
        "other": 0,
    }

    for i in range(len(data)):
        if len(data[i]["comorbidities"]) != 0:
            for j in range(len(data[i]["comorbidities"])):
                if data[i]["comorbidities"][j] in groups["cardiovascular"]:
                    groups_occurence["cardiovascular"] += 1
                if data[i]["comorbidities"][j] in groups["respiratory"]:
                    groups_occurence["respiratory"] += 1
                if data[i]["comorbidities"][j] in groups["metabolic"]:
                    groups_occurence["metabolic"] += 1
                if (
                    data[i]["comorbidities"][j]
                    in groups["neurodegenerative-neocognitive"]
                ):
                    groups_occurence["neurodegenerative-neocognitive"] += 1
                if data[i]["comorbidities"][j] in groups["neoplastic"]:
                    groups_occurence["neoplastic"] += 1
                if data[i]["comorbidities"][j] in groups["other"]:
                    groups_occurence["other"] += 1
    total_comorbidities = sum(groups_occurence.values())
    print("Total number of comorbidities: ", total_comorbidities)
    print("------------------------------")
    print("Comorbidities groups occurence:")
    groups_occurence = sorted(
        groups_occurence.items(), key=lambda x: x[1], reverse=True
    )
    for group, count in groups_occurence:
        print(
            "{:<30} --> {:>5} --> {:>6.2f}%".format(
                group, count, round(int(count) / total_comorbidities * 100, 2)
            )
        )

def compute_pathologies(data: List[Dict]):
    pathologies = {}
    number_of_patients_with_pathologies = 0
    number_of_pathologies = 0
    for i in range(len(data)):
        if len(data[i]["pathologies"]) != 0:
            number_of_patients_with_pathologies += 1
        for j in range(len(data[i]["pathologies"])):
            number_of_pathologies += 1
            if data[i]["pathologies"][j] in pathologies:
                pathologies[data[i]["pathologies"][j]] += 1
            else:
                pathologies[data[i]["pathologies"][j]] = 1
    pathologies = sorted(pathologies.items(), key=lambda x: x[1], reverse=True)
    print(
        "Number of patient with pathologies: ", number_of_patients_with_pathologies
    )
    print("------------------------------")
    print("Number of pathologies: ", number_of_pathologies)
    print("------------------------------")
    print("Pathologies")
    for pathology in pathologies:
        print(
            "{:<70} --> {:>5} --> {:>6.2f}%".format(
                pathology[0],
                pathology[1],
                round(int(pathology[1]) / number_of_pathologies * 100, 2),
            )
        )

def compute_pathologies_year(data: List[Dict], year):
    pathologies = {}
    number_of_patients_with_pathologies = 0
    number_of_pathologies = 0
    for i in range(len(data)):
        deathdate: str = data[i]["deathdate"]
        if int(deathdate.split("-")[0]) == year:
            if len(data[i]["pathologies"]) != 0:
                number_of_patients_with_pathologies += 1
            for j in range(len(data[i]["pathologies"])):
                number_of_pathologies += 1
                if data[i]["pathologies"][j] in pathologies:
                    pathologies[data[i]["pathologies"][j]] += 1
                else:
                    pathologies[data[i]["pathologies"][j]] = 1
    pathologies = sorted(pathologies.items(), key=lambda x: x[1], reverse=True)
    print(
        "Number of patient with pathologies for the year ", year, ": ", number_of_patients_with_pathologies
    )
    print("------------------------------")
    print("Number of pathologies for the year ", year, ": ", number_of_pathologies)
    print("------------------------------")
    print("Pathologies for the year ", year)
    for pathology in pathologies:
        print(
            "{:<70} --> {:>5} --> {:>6.2f}%".format(
                pathology[0],
                pathology[1],
                round(int(pathology[1]) / number_of_pathologies * 100, 2),
            )
        )

def compute_first_pathology(data: List[Dict]):
    pathologies = {}
    number_of_patients_with_pathologies = 0
    for i in range(len(data)):
        if len(data[i]["pathologies"]) != 0:
            number_of_patients_with_pathologies += 1
            if data[i]["pathologies"][0] in pathologies:
                pathologies[data[i]["pathologies"][0]] += 1
            else:
                pathologies[data[i]["pathologies"][0]] = 1
    pathologies = sorted(pathologies.items(), key=lambda x: x[1], reverse=True)
    print("Number of first pathologies: ", number_of_patients_with_pathologies)
    print("------------------------------")
    print("First Pathologies")
    for pathology in pathologies:
        print(
            "{:<70} --> {:>5} --> {:>6.2f}%".format(
                pathology[0],
                pathology[1],
                round(int(pathology[1]) / number_of_patients_with_pathologies * 100, 2),
            )
        )

def compute_first_pathology_year(data: List[Dict], year):
    pathologies = {}
    number_of_patients_with_pathologies = 0
    for i in range(len(data)):
        deathdate: str = data[i]["deathdate"]
        if int(deathdate.split("-")[0]) == year:
            if len(data[i]["pathologies"]) != 0:
                number_of_patients_with_pathologies += 1
                if data[i]["pathologies"][0] in pathologies:
                    pathologies[data[i]["pathologies"][0]] += 1
                else:
                    pathologies[data[i]["pathologies"][0]] = 1
    pathologies = sorted(pathologies.items(), key=lambda x: x[1], reverse=True)
    print("Number of first pathologies for the year ", year, ": ", number_of_patients_with_pathologies)
    print("------------------------------")
    print("First Pathologies for the year ", year)
    for pathology in pathologies:
        print(
            "{:<70} --> {:>5} --> {:>6.2f}%".format(
                pathology[0],
                pathology[1],
                round(int(pathology[1]) / number_of_patients_with_pathologies * 100, 2),
            )
        )

if __name__ == "__main__":
    with open("merged_data_final.json", "r") as data_file:
        data: List[Dict] = json.load(fp=data_file)
    with open("groups.json", "r") as groups_file:
        groups: List[Dict] = json.load(fp=groups_file)

    compute_average_age(data=data)
    print("------------------------------")
    compute_average_age_year(data=data, year=2020)
    print("------------------------------")
    compute_average_age_year(data=data, year=2021)
    print("------------------------------")
    compute_average_age_year(data=data, year=2022)
    print("------------------------------")
    compute_average_age_year(data=data, year=2023)
    print("------------------------------")
    count_male_female(data=data)
    print("------------------------------")
    count_male_female_year(data=data, year=2020)
    print("------------------------------")
    count_male_female_year(data=data, year=2021)
    print("------------------------------")
    count_male_female_year(data=data, year=2022)
    print("------------------------------")
    count_male_female_year(data=data, year=2023)
    print("------------------------------")
    compute_operating_units(data=data)
    print("------------------------------")
    compute_operating_units_year(data=data, year=2020)
    print("------------------------------")
    compute_operating_units_year(data=data, year=2021)
    print("------------------------------")
    compute_operating_units_year(data=data, year=2022)
    print("------------------------------")
    compute_operating_units_year(data=data, year=2023)
    print("------------------------------")
    compute_comorbidities(data=data)
    print("------------------------------")
    compute_comorbidities_year(data=data, year=2020)
    print("------------------------------")
    compute_comorbidities_year(data=data, year=2021)
    print("------------------------------")
    compute_comorbidities_year(data=data, year=2022)
    print("------------------------------")
    compute_comorbidities_year(data=data, year=2023)
    print("------------------------------")
    compute_pure_covid(data=data)
    print("------------------------------")
    compute_pure_covid_year(data=data, year=2020)
    print("------------------------------")
    compute_pure_covid_year(data=data, year=2021)
    print("------------------------------")
    compute_pure_covid_year(data=data, year=2022)
    print("------------------------------")
    compute_pure_covid_year(data=data, year=2023)
    print("------------------------------")
    compute_covid_comorbdities(data=data)
    print("------------------------------")
    compute_covid_comorbdities_year(data=data, year=2020)
    print("------------------------------")
    compute_covid_comorbdities_year(data=data, year=2021)
    print("------------------------------")
    compute_covid_comorbdities_year(data=data, year=2022)
    print("------------------------------")
    compute_covid_comorbdities_year(data=data, year=2023)
    print("------------------------------")
    compute_covid_pathologies(data=data)
    print("------------------------------")
    compute_covid_pathologies_year(data=data, year=2020)
    print("------------------------------")
    compute_covid_pathologies_year(data=data, year=2021)
    print("------------------------------")
    compute_covid_pathologies_year(data=data, year=2022)
    print("------------------------------")
    compute_covid_pathologies_year(data=data, year=2023)
    print("------------------------------")
    compute_pure_covid_no_comorbidities(data=data)
    print("------------------------------")
    compute_pure_covid_no_comorbidities_year(data=data, year=2020)
    print("------------------------------")
    compute_pure_covid_no_comorbidities_year(data=data, year=2021)
    print("------------------------------")
    compute_pure_covid_no_comorbidities_year(data=data, year=2022)
    print("------------------------------")
    compute_pure_covid_no_comorbidities_year(data=data, year=2023)
    print("------------------------------")
    compute_pure_covid_with_comorbidities(data=data)
    print("------------------------------")
    compute_pure_covid_with_comorbidities_year(data=data, year=2020)
    print("------------------------------")
    compute_pure_covid_with_comorbidities_year(data=data, year=2021)
    print("------------------------------")
    compute_pure_covid_with_comorbidities_year(data=data, year=2022)
    print("------------------------------")
    compute_pure_covid_with_comorbidities_year(data=data, year=2023)
    print("------------------------------")
    compute_comorbidities_groups(data=data, groups=groups)
    print("------------------------------")
    compute_pathologies(data=data)
    print("------------------------------")
    compute_pathologies_year(data=data, year=2020)
    print("------------------------------")
    compute_pathologies_year(data=data, year=2021)
    print("------------------------------")
    compute_pathologies_year(data=data, year=2022)
    print("------------------------------")
    compute_pathologies_year(data=data, year=2023)
    print("------------------------------")
    compute_first_pathology(data=data)
    print("------------------------------")
    compute_first_pathology_year(data=data, year=2020)
    print("------------------------------")
    compute_first_pathology_year(data=data, year=2021)
    print("------------------------------")
    compute_first_pathology_year(data=data, year=2022)
    print("------------------------------")
    compute_first_pathology_year(data=data, year=2023)
