import os
import json
import yaml
import subprocess

def json_to_yaml(json_file, yaml_file):
    """Convert JSON file to YAML format."""
    with open(json_file, 'r') as jf:
        json_data = json.load(jf)
    with open(json_file, 'w') as yf:
        yaml.dump(json_data, yf, default_flow_style=False)

def rename_with_git(json_file, yaml_file):
    """Use git to rename the JSON file to YAML."""
    # Use git mv to rename the file
    subprocess.run(['git', 'mv', json_file, yaml_file], check=True)

def check_and_convert_json_to_yaml(base_folder):
    """Iterate through subfolders and convert JSON to YAML if conditions are met."""
    # Iterate through each item in the base folder
    for item in os.listdir(base_folder):
        item_path = os.path.join(base_folder, item)
        
        # Check if the item is a directory (subfolder)
        if os.path.isdir(item_path):
            # Iterate through files in the subfolder
            for file in os.listdir(item_path):
                if file.endswith('.json'):
                    json_file_path = os.path.join(item_path, file)
                    yaml_file_path = os.path.join(item_path, file[:-5] + '.yaml')  # Change .json to .yaml
                    
                    # Check if the corresponding YAML file already exists
                    if not os.path.exists(yaml_file_path):
                        print(f"Converting {json_file_path} to YAML content.")
                        json_to_yaml(json_file_path, yaml_file_path)
                        
                        print(f"Renaming {json_file_path} to {yaml_file_path} using git.")
                        rename_with_git(json_file_path, yaml_file_path)
                        
                        print(f"Successfully converted and renamed {json_file_path} to {yaml_file_path}")
                    else:
                        print(f"YAML file already exists for {json_file_path}: {yaml_file_path}")

# Example usage
base_folder = r'/home/anandhu/CM/repos/anandhu-eng@cm4mlops/script'  # Replace with your folder path
check_and_convert_json_to_yaml(base_folder)
