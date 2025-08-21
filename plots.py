import matplotlib.pyplot as plt
import numpy as np
import json


def plot_age_distribution(data):
    age = []
    for i in range(len(data)):
        try:
            birthdate: str = data[i]["birthdate"]
            deathdate: str = data[i]["deathdate"]
            years_difference: int = int(deathdate.split("-")[0]) - int(
                birthdate.split("-")[0]
            )
            age.append(years_difference)
        except Exception as e:
            print(
                f"[Exception: {e} | Patient with custom-id {data[i]['custom-id']} has birthdate {data[i]['birthdate']} and deathdate {data[i]['deathdate']}"
            )
    age = np.array(age)
    plt.hist(age, bins=max(age), edgecolor="black", alpha=0.7)
    plt.title("Age Distribution of Individuals")
    plt.xlabel("Age")
    plt.ylabel("Number of Individuals")
    plt.grid(axis="y", alpha=0.5)
    plt.tight_layout()
    plt.savefig("age_distribution.png")
    plt.show()
    print("Age distribution plot saved as 'age_distribution.png'")

def plot_age_distribution_10_years_bins(data):
    age = []
    for i in range(len(data)):
        try:
            birthdate: str = data[i]["birthdate"]
            deathdate: str = data[i]["deathdate"]
            years_difference: int = int(deathdate.split("-")[0]) - int(
                birthdate.split("-")[0]
            )
            age.append(years_difference)
        except Exception as e:
            print(
                f"[Exception: {e} | Patient with custom-id {data[i]['custom-id']} has birthdate {data[i]['birthdate']} and deathdate {data[i]['deathdate']}"
            )
    age = np.array(age)
    bins = range(0, max(age) + 10, 10)
    n, bins, patches = plt.hist(age, bins=bins, edgecolor="black", alpha=0.7)
    plt.title("Age Distribution of Individuals (10-Year Bins)")
    # Create interval labels like '0-10', '10-20', etc.
    interval_labels = [f"{bins[i]:.0f}-{bins[i+1]:.0f}" for i in range(len(bins)-1)]
    plt.xlabel("Age Interval")
    plt.ylabel("Number of Individuals")
    plt.xticks([(bins[i] + bins[i+1]) / 2 for i in range(len(bins)-1)], interval_labels, rotation=45)
    # Add count numbers on top of each bar
    for i in range(len(n)):
        plt.text((bins[i] + bins[i+1]) / 2, n[i], str(int(n[i])), ha='center', va='bottom', fontsize=8)
    plt.tight_layout()
    plt.grid(axis="y", alpha=0.5)
    plt.savefig("age_distribution_10_year_bins.png")
    plt.show()
    print("Age distribution plot saved as 'age_distribution_10_year_bins.png'")

def plot_age_per_year_distribution(data):
    age_2020 = []
    age_2021 = []
    age_2022 = []
    age_2023 = []
    for i in range(len(data)):
        try:
            birthdate: str = data[i]["birthdate"]
            deathdate: str = data[i]["deathdate"]
            year_of_birth = int(birthdate.split("-")[0])
            year_of_death = int(deathdate.split("-")[0])
            if year_of_death == 2020:
                age_2020.append(year_of_death - year_of_birth)
            elif year_of_death == 2021:
                age_2021.append(year_of_death - year_of_birth)
            elif year_of_death == 2022:
                age_2022.append(year_of_death - year_of_birth)
            elif year_of_death == 2023:
                age_2023.append(year_of_death - year_of_birth)
        except Exception as e:
            print(
                f"[Exception: {e} | Patient with custom-id {data[i]['custom-id']} has birthdate {data[i]['birthdate']} and deathdate {data[i]['deathdate']}"
            )
    age_2020 = np.array(age_2020)
    age_2021 = np.array(age_2021)
    age_2022 = np.array(age_2022)
    age_2023 = np.array(age_2023)

    # Combine all ages to get bin range
    all_ages = np.concatenate([age_2020, age_2021, age_2022, age_2023])
    bins = range(0, max(all_ages) + 10, 10)
    colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']  # blue, orange, green, red
    labels = ['2020', '2021', '2022', '2023']
    age_groups = [age_2020, age_2021, age_2022, age_2023]

    plt.figure(figsize=(10, 6))
    # Plot stacked filled histograms
    counts, bins, patches = plt.hist(age_groups, bins=bins, stacked=True, color=colors, edgecolor="black", alpha=0.7, label=labels)
    # Add count numbers on top of each bar for each year
    # Invert the shape on counts
    counts = np.array(counts).T  # Transpose to match the shape of bins
    print("Counts:", counts)
    for i in range(len(counts)):
        for j in range(len(colors)):
            if j == 0:
                plt.text((bins[i] + bins[i+1]) / 2, counts[i][-1] + 11 * j, str(int(counts[i][j])), ha='center', va='bottom', fontsize=8, color=colors[j])
            else:
                plt.text((bins[i] + bins[i+1]) / 2, counts[i][-1] + 11 * j, str(int(counts[i][j]) - int(counts[i][j-1])), ha='center', va='bottom', fontsize=8, color=colors[j])

    plt.title("Age Distribution by Year of Death (10-Year Bins)")
    interval_labels = [f"{bins[i]:.0f}-{bins[i+1]:.0f}" for i in range(len(bins)-1)]
    plt.xlabel("Age Interval")
    plt.ylabel("Number of Individuals")
    plt.xticks([(bins[i] + bins[i+1]) / 2 for i in range(len(bins)-1)], interval_labels, rotation=45)
    plt.ylim(top=max(counts.flatten() + 50))
    plt.legend()
    plt.tight_layout()
    plt.grid(axis="y", alpha=0.5)
    plt.savefig("age_distribution_per_year_10_year_bins.png")
    plt.show()
    print("Age distribution per year plot saved as 'age_distribution_per_year_10_year_bins.png'")

if __name__ == "__main__":
    with open("merged_data_final.json", "r") as data_file:
        data = json.load(data_file)

    plot_age_distribution(data=data)
    plot_age_distribution_10_years_bins(data=data)
    plot_age_per_year_distribution(data=data)
