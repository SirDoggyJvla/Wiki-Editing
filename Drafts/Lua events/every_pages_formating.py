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


def format_event_page(events, format_file_path,file_path):
    with open(format_file_path, 'r') as format_file:
        format_string = format_file.read()

    for eventName in events:
        file_name = f"{file_path}\{eventName}.wt"
        
        this_event_data = event_data["events"][eventName]
        
        # PARAMETERS
        paramsListing = ""
        paramsFunction = ""
        if 'callback' in this_event_data:
            if 'parameters' in this_event_data['callback']:
                parameters = this_event_data['callback']['parameters']
                
                if len(parameters) == 0:
                    paramsListing = "No parameters."
                else:
                    for param in this_event_data['callback']['parameters']:
                        paramsListing += f"*{param['name']}: [[{param['type']}]]"
                        if 'notes' in param:
                            paramsListing += f" - {param['notes']}"
                        paramsListing += "\n"
                        paramsFunction += f"{param['name']}, "
                    paramsListing = paramsListing[:-1]
                    paramsFunction = paramsFunction[:-2]
            else:
                paramsListing = "No parameters."
        
        # CONTEXT
        eventListing = ""
        if 'context' in this_event_data:
            context = this_event_data['context']
            if 'singleplayer' in context and not context['singleplayer']:
                eventListing += "(Multiplayer only) "
            
            if 'server' in context and not context['server']:
                eventListing += "(Client) "
            
            if 'client' in context and not context['client']:
                eventListing += "(Server) "

        eventListing += f"{eventName}"
        
        # NOTES
        notes = ""
        if 'notes' in this_event_data:
            notes = this_event_data['notes']
        
        
        
        

        # WRITE TO FILE
        with open(file_name, 'w') as file:
            file.write(format_string.format(eventName=eventName,
                                            paramsListing=paramsListing,
                                            paramsFunction=paramsFunction,
                                            eventListing=eventListing,
                                            notes=notes)
                       )

page_formating_current = r"C:\Users\simon\Documents\Perso\Jeux\Zomboid\Wiki\Drafts\Lua events\current_formating.wt"
page_formating_deprecated = r"C:\Users\simon\Documents\Perso\Jeux\Zomboid\Wiki\Drafts\Lua events\deprecated_formating.wt"
file_path = r"C:\Users\simon\Documents\Perso\Jeux\Zomboid\Wiki\Drafts\Lua events\events"

format_event_page(current_events, page_formating_current,file_path)