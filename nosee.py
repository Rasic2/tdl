import json
from pathlib import Path

total = []
for file in Path("jsons").iterdir():
    with open(file, "r") as f:
        #print(file)
        json_object = json.load(f)
        for item in json_object['messages']:
            item.update({'item_id': json_object["id"]})
            total.append(item)

sorted_total = sorted(total, key=lambda x: x['emoji_count'], reverse=True)

with open("tdl-chatlist", "r") as f:
    content = f.readlines()

exist_ids = [line.split()[0] for line in content[1:]]
#print(exist_ids)
count = 0
exist_count = {}
for item in sorted_total:
    if str(item["item_id"]).strip() not in exist_ids:
        print("\033[1;31m",item["item_id"], "is expired!", "\033[0m")
        continue
    file_exist = Path(f'downloads/{item["item_id"]}').glob(f'{item["item_id"]}_{item["id"]}_*')
    if not (list(file_exist)):
        count += 1
        exist_count[item["item_id"]]=exist_count.get(item["item_id"], 0)+1
        print(exist_count[item["item_id"]], item["item_id"], item["file"], item["emoji_count"])
    if count >= 40:
        break
pass
