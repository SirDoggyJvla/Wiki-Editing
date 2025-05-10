import json

# Path to the JSON file
json_file_path = r"C:\Users\simon\Documents\Perso\Jeux\Zomboid\Wiki\Wiki-Editing\Drafts\Lua (API)\Lua objects\ISBaseTimedAction.json"

object_name = "ISBaseTimedAction"

# Load and parse the JSON file
with open(json_file_path, 'r', encoding='utf-8') as file:
    data = json.load(file)


# Write the generated lines to a file named after the object_name
path = r"C:\Users\simon\Documents\Perso\Jeux\Zomboid\Wiki\Wiki-Editing\Drafts\Lua (API)\Lua objects"
file = f"{object_name}_functions.wt"

output_file_path = f"{path}\\{file}"

with open(output_file_path, 'w', encoding='utf-8') as output_file:
    for key, value in data["functions"].items():
        line = "{{Function|function="
        
        if "static" in value:
            line += f"{object_name}.{key}("
        else:
            line += f"{object_name}:{key}("
        
        params = value["parameters"]
        
        for param in params:
            line += param["name"] + ","

        # remove the last comma
        if len(params) > 0:
            line = line[:-1]
        
        line += ")|"
        
        # setup the function description
        if value["description"]:
            line += "description=" + value["description"] + "|"
        
        for param in params:
            line += "\n{{Function/param|name=" + param["name"]

            if "type" in param:
                line += "|type=" + param["type"]
            
            if "description" in param:
                line += "|description=" + param["description"]
            
            line += "}}"
            
            # if "error" in param:
            #     line += "\n{{Note|type=error|" + param["error"] + "}}"
            
        line += "|"
        
        if "returns" in value:
            for rtn in value["returns"]:
                line += "\n{{Function/param|name=" + rtn["name"]

                if rtn["type"]:
                    line += "|type=" + rtn["type"]
                
                if rtn["description"]:
                    line += "|description=" + rtn["description"]
                    
                line += "}}"
            
        line += "}}"

        output_file.write(line + "\n")
        
        
file = f"{object_name}_variables.wt"

output_file_path = f"{path}\\{file}"

with open(output_file_path, 'w', encoding='utf-8') as output_file:
    first = False
    for key, value in data["variables"].items():
        line = "----"
        
        line += "{{Function/param|name=" + key + "|"
        line += "type=" + value["type"] + "|"
        line += "description=" + value["description"] + "|"
        
        if "default" in value:
            line += "default=" + str(value["default"])
            
        line += "}}\n"

        output_file.write(line)