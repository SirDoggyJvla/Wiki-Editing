import json
import os


class FormatEvents:
    def __init__(self, json_path):
        self.json_path = json_path
        self.current_events = []
        self.deprecated_events = []
        self.event_data = self.get_events(json_path)

    def get_events(self,json_path):
        with open(json_path, 'r') as file:
            event_data = json.load(file)
        
        for key,value in event_data["events"].items():
            if 'deprecated' in value:
                self.deprecated_events.append(key)
            else:
                self.current_events.append(key)
        
        return event_data
                
        # # probably not needed
        # self.current_events.sort() 
        # self.deprecated_events.sort()
        
    PARAM_TO_WIKI = {}
    PARAM_TO_NOLINK = {
        "string": "string",
        "integer": "integer",
        "float": "float",
        "boolean": "boolean",
        "table": "table",
        "number": "number",
    }
    TYPE_URLS: list[tuple[str, dict[str, str]]] = [
        ("https://demiurgequantified.github.io/ProjectZomboidJavaDocs/", {
            "IsoGameCharacter": "zombie/characters/IsoGameCharacter",
            "PerkFactory.Perk": "zombie/characters/skills/PerkFactory.Perk",
            "ObjectTooltip": "zombie/ui/ObjectTooltip/ObjectTooltip",
            "IsoGridSquare": "zombie/iso/IsoGridSquare",
            "State": "zombie/ai/State",
            "ChatMessage": "zombie/chat/ChatMessage",
            "IsoPlayer": "zombie/characters/IsoPlayer",
            "ClimateManager": "zombie/iso/weather/ClimateManager",
            "IsoLivingCharacter": "zombie/characters/IsoLivingCharacter",
            "SurvivorDesc": "zombie/characters/SurvivorDesc",
            "IsoSurvivor": "zombie/characters/IsoSurvivor",
            "IsoThumpable": "zombie/iso/objects/IsoThumpable",
            "WaveSignalDevice": "zombie/radio/devices/WaveSignalDevice",
            "MovableRecipe": "zombie/scripting/objects/MovableRecipe",
            "Moveable": "zombie/inventory/types/Moveable",
            "InventoryItem": "zombie/inventory/InventoryItem",
            "ItemContainer": "zombie/inventory/ItemContainer",
            "IsoObject": "zombie/iso/IsoObject",
            "DBResult": "zombie/network/DBResult",
            "IsoZombie": "zombie/characters/IsoZombie",
            "BodyPartType": "zombie/characters/BodyDamage/BodyPartType",
            "HandWeapon": "zombie/inventory/types/HandWeapon",
            "WeatherPeriod": "zombie/iso/weather/WeatherPeriod",
            "WeatherPeriod.WeatherStage": "zombie/iso/weather/WeatherPeriod.WeatherStage",
            "RecordedMedia": "zombie/radio/media/RecordedMedia",
            "ErosionSeason": "zombie/erosion/season/ErosionSeason",
            "IsoSpriteManager": "zombie/iso/sprite/IsoSpriteManager",
            "RadioScriptManager": "zombie/radio/scripting/RadioScriptManager",
            "BuildingDef": "zombie/iso/BuildingDef",
            "IsoFire": "zombie/iso/objects/IsoFire",
            "IsoMovingObject": "zombie/iso/IsoMovingObject",
            "IsoCell": "zombie/iso/IsoCell",
            "IsoRoom": "zombie/iso/areas/IsoRoom",
            "Server": "zombie/network/Server",
            "IsoTrap": "zombie/iso/objects/IsoTrap",
            "BaseVehicle": "zombie/vehicles/BaseVehicle",
            "Recipe": "zombie/scripting/objects/Recipe",
            "Recipe.Result": "zombie/scripting/objects/Recipe.Result",
            "Item": "zombie/scripting/objects/Item",
            "VehiclePart": "zombie/vehicles/VehiclePart",
            "IsoAnimal": "zombie/characters/animals/IsoAnimal",
            "IsoChunk": "zombie/iso/IsoChunk",
            "ContainerID": "zombie/network/fields/ContainerID",
            "IsoDeadBody": "zombie/iso/objects/IsoDeadBody",
            "AnimalTracks": "zombie/characters/animals/AnimalTracks",
            "CraftRecipeData": "zombie/entity/components/crafting/recipe/CraftRecipeData"
        }),
        ("https://docs.oracle.com/en/java/javase/17/docs/api/", {
            "ArrayList": "java.base/java/util/ArrayList",
            "Object": "java.base/java/lang/Object"
        })
    ]
    
    def get_class_link(self,clazz):
        """
        Returns the link to a class's API page if it exists, else returns the input name

        :param clazz: The name of the class
        :return: Link to the class's API page or plain text name
        """
        for domain in self.TYPE_URLS:
            url = domain[1].get(clazz)
            if url is not None:
                return f"{domain[0]}{url}.html"
    
        
    def format_parameters(self, event_data):
        paramsListing = ""
        paramsFunction = ""
        if 'callback' in event_data:
            if 'parameters' in event_data['callback']:
                parameters = event_data['callback']['parameters']
                
                if len(parameters) == 0:
                    paramsListing = "No parameters."
                else:
                    # for each parameters
                    for param in event_data['callback']['parameters']:
                        type = param['type']
                        skip_notes = False

                        # case where no link should be done, likeif arraytype of object
                        if type in self.PARAM_TO_NOLINK or '<' in type or '>' in type:
                            paramsListing += f"*{param['name']}: {type}"
                        elif "|" in type:
                            types = type.split("|")
                            paramsListing += f"*{param['name']}"
                            if 'notes' in param:
                                paramsListing += f" - {param['notes']}"
                                skip_notes = True
                                
                            paramsListing += "\n"
                            
                            for t in types:
                                paramsListing += f"**{t}\n"
                            paramsListing = paramsListing[:-1] # remove last "\n"
                        else:
                            # link to wiki page of object
                            if type.endswith("[]"):
                                type = type[:-2]
                                paramsListing += f"*{param['name']}: [[{type}]][]"
                            else:
                                paramsListing += f"*{param['name']}: [[{type}]]"

                        # retrieve java doc link if exists
                        #TODO: add multiple java doc links for multiple mentions of different java objects
                        # i.e. ArrayList<Object> -> [link ArrayList], [link Object]
                        java_doc = self.get_class_link(type)
                        if java_doc is not None:
                            paramsListing += f" ([{java_doc} JavaDoc])"
                        
                        # add notes
                        if not skip_notes and 'notes' in param:
                            paramsListing += f" - {param['notes']}"
                        paramsListing += "\n"
                        paramsFunction += f"{param['name']}, "
                        
                    # remove last "\n", or ", " for functions
                    paramsListing = paramsListing[:-1]
                    paramsFunction = paramsFunction[:-2]
            else:
                paramsListing = "No parameters."
                
        return paramsListing, paramsFunction
    
    def format_context(self, event_data, eventName):
        eventListing = ""
        if 'context' in event_data:
            context = event_data['context']
            if 'singleplayer' in context and not context['singleplayer']:
                eventListing += "(Multiplayer only) "
            
            if 'server' in context and not context['server']:
                eventListing += "(Client) "
            
            if 'client' in context and not context['client']:
                eventListing += "(Server) "

        eventListing += f"{eventName}"
        
        return eventListing

    def format_pages(self, events, format_file_path,file_path,format=".txt"):        
        with open(format_file_path, 'r') as format_file:
            page_formating = format_file.read()
            
        events_data = self.event_data["events"]
        for eventName in events:
            file_name = f"{file_path}\{eventName}{format}"
            event_data = events_data[eventName]
            
            # PARAMETERS
            paramsListing, paramsFunction = self.format_parameters(event_data)
            
            # CONTEXT
            eventListing = self.format_context(event_data, eventName)
            
            # NOTES
            notes = ""
            if 'notes' in event_data:
                notes = event_data['notes']

            print(paramsListing)
            
            
            # WRITE TO FILE
            with open(file_name, 'w') as file:
                file.write(page_formating.format(eventName=eventName,
                                                paramsListing=paramsListing,
                                                paramsFunction=paramsFunction,
                                                eventListing=eventListing,
                                                notes=notes))
            
            
            
            
if __name__ == "__main__":
    json_path = r"C:/Users/simon/Documents/Perso/Jeux/Zomboid/Wiki/Wiki-Editing/Drafts/Lua events/PZEventDoc/data.json"
    format_path = r"C:/Users/simon/Documents/Perso/Jeux/Zomboid/Wiki/Wiki-Editing/Drafts/Lua events/current_formating.wt"
    file_path = r"C:/Users/simon/Documents/Perso/Jeux/Zomboid/Wiki/Wiki-Editing/Drafts/Lua events/events"
    format_events = FormatEvents(json_path)
    format_events.format_pages(format_events.current_events, format_path, file_path)
