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
count = 0
for meg in messages:
    if 'emoji_count' in meg.keys() and meg['emoji_count'] > 30:
        count+=1
        if meg['id'] not in files:
            reduced_messages.append(meg)
    if count >= 100:
        break
sorted_reduced_messages = sorted(reduced_messages, key=lambda x:x['emoji_count'], reverse=True)
print(f"--> Total download files needed: {len(sorted_reduced_messages)}")

content_n = {'id': id, 'messages': sorted_reduced_messages}
with open("tdl-export-reduced.json", "w") as f:
    json.dump(content_n, f)
