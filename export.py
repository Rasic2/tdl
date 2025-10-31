import json
import os
import sys
from pathlib import Path

JSONDir = "./jsons"
DefaultJson = "tdl-export.json"

id = sys.argv[1]
id_json = Path(f"{JSONDir}/{id}.json")
if not id_json.exists():
    os.system(f"go run main.go chat export -c {id} -T id -i 0,1001")
else:
    with open(id_json, "r") as f:
        json_content = json.load(f)
    messages = json_content['messages']
    all_ids = [meg['id'] for meg in messages]
    
    if all_ids:
        max_id = max(all_ids)
        os.system(f"go run main.go chat export -c {id} -T id -i {max_id + 1},{max_id + 1001}")
    else:
        max_id = 0
        os.system(f"go run main.go chat export -c {id} -T id -i {max_id + 1}")
    print("max_id = ", max_id)
    with open(DefaultJson, "r") as f:
        default_content = json.load(f)

    assert str(default_content['id']) == str(json_content['id'])

    default_messages = default_content['messages']
    final_messages = messages + [meg for meg in default_messages if meg['id'] not in all_ids]

    final_content = {'id': id, 'messages': final_messages}
    with open(DefaultJson, "w") as f:
        json.dump(final_content, f)

os.system(f"cp {DefaultJson} {JSONDir}/{id}.json")
