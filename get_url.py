import sys
import json
from pathlib import Path

RootUrl = "https://t.me/"

with open("tdl-export-reduced.json", "r") as f:
    content = json.load(f)

messages = content['messages']

with open("tdl-chatlist", "r") as f:
    chatlist = f.readlines()

for group in chatlist:
    if sys.argv[1] in group.split():
        username = group.split()[-2]
        break

for msg in messages:
    print(RootUrl + username + "/" + str(msg['id']))

#files = [int(file.stem.split("_")[1]) for file in Path(f"downloads/{id}").iterdir()]
#reduced_messages = []
#for meg in messages:
#    if meg['id'] not in files:
#        reduced_messages.append(meg)

#content_n = {'id': id, 'messages': reduced_messages}
#with open("tdl-export-reduced.json", "w") as f:
#    json.dump(content_n, f)
