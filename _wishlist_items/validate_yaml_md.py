import os
import sys
import yaml

def is_valid_yaml_front_matter(content):
    if not content.startswith('---'):
        return False, "No starting '---'"
    
    try:
        parts = content.split('---', 2)
        if len(parts) < 3:
            return False, "No ending '---'"
        yaml_content = parts[1]
        yaml.safe_load(yaml_content)
        return True, None
    except yaml.YAMLError as e:
        return False, str(e)

def validate_md_files(folder_path):
    failed = []

    for filename in os.listdir(folder_path):
        if filename.endswith('.md'):
            path = os.path.join(folder_path, filename)
            with open(path, 'r', encoding='utf-8') as file:
                content = file.read()
                valid, error = is_valid_yaml_front_matter(content)
                if not valid:
                    failed.append((filename, error))
    
    if failed:
        for filename, error in failed:
            print(f"[FAIL]  {filename}: {error}")
    else:
        print("No errors found")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python validate_yaml_md.py <folder_path>")
        sys.exit(1)
    
    folder = sys.argv[1]
    validate_md_files(folder)

