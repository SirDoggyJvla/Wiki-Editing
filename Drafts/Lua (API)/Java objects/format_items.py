import json

file = "/home/simon/Documents/Repositories/pz-wiki_parser/data/item_data.json"

unique = {}
with open(file, "r") as f:
    data = json.load(f)
    for item in data.values():
        if "Type" in item:
            unique[item["Type"]] = item

s = "*{{{{JavaObject|{0}|package=zombie/inventory/types|customDoc=https://demiurgequantified.github.io/ProjectZomboidJavaDocs/}}}}"
for k, v in unique.items():
    print(s.format(k))

print()
for k, v in unique.items():
    print("*" + k)


