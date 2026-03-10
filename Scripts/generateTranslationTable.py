import os, yaml, pyperclip, json

DATA_PATH = os.path.join("pz-scripts-data", "data")
TRANSLATION_DATA_PATH = os.path.join(DATA_PATH, "translation_files")

txt = ""
for filename in os.listdir(TRANSLATION_DATA_PATH):
    if filename.endswith(".yaml"):
        with open(os.path.join(TRANSLATION_DATA_PATH, filename), "r") as f:
            data = yaml.safe_load(f)

            keyPrefix = data.get("keyPrefix", None)
            if keyPrefix is not None:
                keyPrefix = f"<code>{keyPrefix}</code>"
            else:
                keyPrefix = ""

            function = data.get("function", None)
            if function is not None:
                function = f"<code>{function}</code>"
            else:
                function = ""

            description = data.get("description", "")
            
            txt += f"|-\n| {data['fileName']} || {keyPrefix} || {function} ||\n{description}\n"

pyperclip.copy(txt)

input("Press enter to continue")

LANGUAGE_DATA_PATH = os.path.join(DATA_PATH, "languageCodes.json")

with open(LANGUAGE_DATA_PATH, "r") as f:
    language_data = json.load(f)

txt = ""
for language in language_data:
    encoding = language.get("encoding", "UTF-8")
    txt 

