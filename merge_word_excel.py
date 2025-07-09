import json
import pandas as pd


def convert_birthdate(date_str, operating_unit=None):
    """Convert date string from 'Jan-36' to '1936-01'."""
    month_map = {
        "Jan": "01",
        "Feb": "02",
        "Mar": "03",
        "Apr": "04",
        "May": "05",
        "Jun": "06",
        "Jul": "07",
        "Aug": "08",
        "Sep": "09",
        "Oct": "10",
        "Nov": "11",
        "Dec": "12",
    }
    if str(date_str) == "nan":
        return None

    parts = date_str.split("-")
    if len(parts) != 2:
        raise ValueError(f"Invalid date format: {date_str}")

    month = month_map.get(parts[0])
    if not month:
        raise ValueError(f"Invalid month in date: {date_str}")

    year = parts[1]
    if len(year) == 2:
        if operating_unit == "neonatol":
            year = "20" + year
        else:
            year = "19" + year
    elif len(year) == 4:
        year = year
    else:
        raise ValueError(f"Invalid year in date: {date_str}")

    return f"{year}-{month}"


def convert_deathdate(date_str):
    """Convert date string from 'DD/MM/YYYY' to 'YYYY-MM-DD'."""
    if not date_str:
        return None
    parts = date_str.split("/")
    if len(parts) != 3:
        raise ValueError(f"Invalid date format: {date_str}")
    day, month, year = parts
    if len(year) == 2:
        year = "20" + year
    elif len(year) != 4:
        raise ValueError(f"Invalid year in date: {date_str}")

    return f"{year}-{month.zfill(2)}-{day.zfill(2)}"


def convert_covid_positive(value):
    """Convert 'si'/'no' to boolean."""
    if "si" in value.lower():
        return True
    elif "no" in value.lower():
        return False
    elif "sospetto" in value.lower():
        return None
    else:
        raise ValueError(f"Invalid value for covid-positive: {value}")


if __name__ == "__main__":
    with open("temp.json", "r") as json_file:
        subjects = json.load(json_file)

    with open("temp.csv", "r") as csv_file:
        csv_data = pd.read_csv(csv_file)

    if len(subjects) != len(csv_data):
        raise ValueError(
            "The number of subjects in JSON does not match the number of rows in CSV."
        )

    for i in range(len(subjects)):
        subjects[i]["id"] = i
        subjects[i]["custom-id"] = i + 2
        subjects[i]["year-file"] = "2020-2022"
        subjects[i]["gender"] = csv_data.iloc[i]["sesso"]
        subjects[i]["birthdate"] = convert_birthdate(
            csv_data.iloc[i]["data_nascita"], csv_data.iloc[i]["unita_operativa"]
        )
        subjects[i]["deathdate"] = convert_deathdate(csv_data.iloc[i]["data_morte"])
        subjects[i]["operating_unit"] = csv_data.iloc[i]["unita_operativa"]
        subjects[i]["covid-positive"] = convert_covid_positive(
            csv_data.iloc[i]["esito_covid"]
        )
        subjects[i]["cause-of-death"] = subjects[i]["pathologies"][-1]

    with open("merged_data.json", "w") as merged_file:
        json.dump(subjects, merged_file, indent=4)
