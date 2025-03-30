import json

# Path to the JSON file
json_file_path = r"C:\Users\simon\Documents\Perso\Jeux\Zomboid\Wiki\Wiki-Editing\Drafts\Lua (API)\Lua objects\ISBaseTimedAction.json"

# Load and parse the JSON file
with open(json_file_path, 'r', encoding='utf-8') as file:
    data = json.load(file)

for key, value in data["functions"].items():
    # Print the function name and its description
    print(f"Function: {key}")
    print(f"Description: {value['description']}")
    print("Parameters:")
    
    # Print the parameters and their descriptions
    for param in value["parameters"]:
        param_name = param["name"]
        param_description = param["description"]
        print(f"  - {param_name}: {param_description}")
    
    print()  # Print a newline for better readability