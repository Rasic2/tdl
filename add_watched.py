import os
import sys
import json
from pathlib import Path

with open("tdl-export.json", "r") as f:
    content = json.load(f)

id = content['id']
messages = content['messages']

for index, meg in enumerate(messages[::-1]):
    cur_group_id = meg['group_id']
    if index == 0:
        last_group_id = meg['group_id']
    if index > 0 and cur_group_id != 0 and cur_group_id == last_group_id:
        meg['emoji_count'] = last_emoji_count
    else:
        last_emoji_count = meg['emoji_count']
        last_group_id = meg['group_id']

os.system(f"rm -rf downloads/{id}/.DS_Store")
os.system(f"rm -rf downloads/{id}/*.tmp")
files = [int(file.stem.split("_")[1]) for file in Path(f"downloads/{id}").iterdir()]

with open("watched","r") as f:
    stored = [line.split(",")[0]+"_"+line.split(",")[1] for line in f.readlines()]

structed_messages = {str(meg['id']):[meg['emoji_count'],meg['file']]  for meg in messages}
for file in files:
    if (f"{id}_{file}" not in stored):
        with open("watched","a") as f:
            try:
                f.write(f"{id},{file},{structed_messages[str(file)][0]},{structed_messages[str(file)][1]}\n")
            except KeyError:
                print(f"{file} is not exist")
