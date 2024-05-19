import json
from pathlib import Path

total = []
for file in Path("jsons").iterdir():
    with open(file, "r") as f:
        json_object = json.load(f)
        for item in json_object['messages']:
            item.update({'item_id': json_object["id"]})
            total.append(item)

sorted_total = sorted(total, key=lambda x: x['emoji_count'], reverse=True)

count = 0
for item in sorted_total:
    if not Path(f'downloads/{item["item_id"]}/{item["item_id"]}_{item["id"]}_{item["file"]}').exists():
        count += 1
        print(item["item_id"], item["file"], item["emoji_count"])
    if count >= 10:
        break
pass
