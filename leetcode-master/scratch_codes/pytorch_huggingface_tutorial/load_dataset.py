"""
!wget https://github.com/crux82/squad-it/raw/master/SQuAD_it-train.json.gz
!wget https://github.com/crux82/squad-it/raw/master/SQuAD_it-test.json.gz

!gzip -dkv SQuAD_it-*.json.gz
"""

from datasets import load_dataset

squad_it_dataset = load_dataset("json", data_files="SQuAD_it-train.json", field="data")


print(f"squad_it_dataset -> {squad_it_dataset}")

# DatasetDict({
#     train: Dataset({
#         features: ['title', 'paragraphs'],
#         num_rows: 442
#     })
# })

print(f"squad_it_dataset_train_split -> {squad_it_dataset["train"][0]}")

# {
#     "title": "Terremoto del Sichuan del 2008",
#     "paragraphs": [
#         {
#             "context": "Il terremoto del Sichuan del 2008 o il terremoto...",
#             "qas": [
#                 {
#                     "answers": [{"answer_start": 29, "text": "2008"}],
#                     "id": "56cdca7862d2951400fa6826",
#                     "question": "In quale anno si è verificato il terremoto nel Sichuan?",
#                 },
#                 ...
#             ],
#         },
#         ...
#     ],
# }