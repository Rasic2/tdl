with open("watched", "r") as f:
    content = [line.split(",")[0] for line in f.readlines()]

sorted_list = []
for item in content:
    if item not in sorted_list:
        sorted_list.append(item)
        print(sorted_list.index(item)+1, item)
