import os
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
reduced_messages = []
for meg in messages:
    if 'emoji_count' in meg.keys() and meg['emoji_count'] > 30 and meg['id'] not in files:
        reduced_messages.append(meg)
sorted_reduced_messages = sorted(reduced_messages, key=lambda x:x['emoji_count'], reverse=True)

content_n = {'id': id, 'messages': sorted_reduced_messages}
with open("tdl-export-reduced.json", "w") as f:
    json.dump(content_n, f)
