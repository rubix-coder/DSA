"""
!wget "https://archive.ics.uci.edu/ml/machine-learning-databases/00462/drugsCom_raw.zip"
!unzip drugsCom_raw.zip
"""

from datasets import load_dataset

data_files = {"train": "drugsComTrain_raw.tsv", "test": "drugsComTest_raw.tsv"}
# \t is the tab character in Python
drug_dataset = load_dataset("csv", data_files=data_files, delimiter="\t")

drug_sample = drug_dataset["train"].shuffle(seed=42).select(range(1000))
# Peek at the first few examples
print(f"peek_view_samples -> {drug_sample[:3]}")

for split in drug_dataset.keys():
    assert len(drug_dataset[split]) == len(drug_dataset[split].unique("Unnamed: 0"))

drug_dataset = drug_dataset.rename_column(
    original_column_name="Unnamed: 0", new_column_name="patient_id"
)

print(f"drug_dataset_sample -> {drug_dataset}")

def lowercase_condition(example):
    return {"condition": example["condition"].lower()}

def filter_nones(x):
    return x["condition"] is not None

drug_dataset = drug_dataset.filter(lambda x: x["condition"] is not None)

drug_dataset.map(lowercase_condition)

drug_dataset = drug_dataset.map(lowercase_condition)
# Check that lowercasing worked

print(f'check if lower casing worked -> {drug_dataset["train"]["condition"][:3]}')
