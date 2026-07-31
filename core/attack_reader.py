import json

file_path="data/enterprise-attack.json"
with open(file_path, "r") as f:
    data= json.load(f)

print("Top-level keys: ")
print(list(data.keys()))

print("\nNumber of ATT&CK objects: ")
print (len(data["objects"]))

#COUNT ATTACK PATTERN OBJECTS

technique_count = 0
for obj in data["objects"]:
    if obj.get("type") == "attack-pattern":
        technique_count += 1

print("\nNumber of ATT&CK techniques: ")
print(technique_count)
