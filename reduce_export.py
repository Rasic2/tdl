import json
from pathlib import Path

with open("tdl-export.json", "r") as f:
    content = json.load(f)

id = content['id']
messages = content['messages']

files = [int(file.stem.split("_")[1]) for file in Path(f"downloads/{id}").iterdir()]
reduced_messages = []
for meg in messages:
    if meg['id'] not in files:
        reduced_messages.append(meg)

content_n = {'id': id, 'messages': reduced_messages}
with open("tdl-export-reduced.json", "w") as f:
    json.dump(content_n, f)
