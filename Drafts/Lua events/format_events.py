import json

def load_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

file_path = r"C:\Users\simon\Documents\Perso\Jeux\Zomboid\Wiki\Drafts\Lua events\PZEventDoc\data.json"
event_data = load_json(file_path)

current_events = []
deprecated_events = []

for key,value in event_data["events"].items():
    if 'deprecated' in value:
        deprecated_events.append(key)
    else:
        current_events.append(key)
        
current_events.sort()
deprecated_events.sort()

def format_events_to_csv(events, columns=5):
    csv_string = ""
    for i, event in enumerate(events):
        if i % columns == 0 and i != 0:
            csv_string += "\n"
        csv_string += f"[[{event}]]" + ("," if (i + 1) % columns != 0 else "")
    return csv_string

current_csv = format_events_to_csv(current_events,columns = 4)
deprecated_csv = format_events_to_csv(deprecated_events)

print("Current Events:\n")
print(current_csv)
print("\n\nDeprecated Events:\n")
print(deprecated_csv)


def format_events_to_csv(events):
    csv_string = "<div class=\"list-columns\">\n"
    for i, event in enumerate(events):
        csv_string += f"*[[{event}]]\n"
    csv_string += "</div>"
    return csv_string

current_csv = format_events_to_csv(current_events)
deprecated_csv = format_events_to_csv(deprecated_events)

print("Current Events:\n")
print(current_csv)
print("\n\nDeprecated Events:\n")
print(deprecated_csv)