import yaml, os, json
from pprint import pprint

PROJECT_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..')
SCRIPT_BLOCK_PATH = os.path.join(PROJECT_PATH, 'pz-scripts-data', 'data', 'blocks')
OUTPUT_PATH = os.path.join(PROJECT_PATH, 'Drafts', 'Scripts', 'GeneratedPages')
FILENAME = '{param_name} ({block_name} parameter).wt'

# list blocks
blocks = {}
for block_file in os.listdir(SCRIPT_BLOCK_PATH):
    print(block_file)
    if block_file.endswith('.yaml'):
        block_name = block_file[:-5]
        with open(os.path.join(SCRIPT_BLOCK_PATH, block_file), 'r') as f:
            block_data = yaml.safe_load(f)
            blocks[block_name] = block_data


for block_name, block_data in blocks.items():
    parameters = block_data.get('parameters', [])
    for param_data in parameters:
        param_name = param_data['name']
        param_desc = param_data.get('description')
        
        filename = FILENAME.format(param_name=param_name, block_name=block_name)
        print(filename)
        output_file_path = os.path.join(OUTPUT_PATH, block_name, filename)
        os.makedirs(os.path.dirname(output_file_path), exist_ok=True)
        with open(output_file_path, 'w', encoding='utf-8') as f:
            f.write(f'# {param_name} ({block_name} parameter)\n\n')
            if param_desc:
                f.write(f'{param_desc}\n')