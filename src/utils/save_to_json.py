import json
import os

def save_list_to_json_files(data, output_file_prefix, folder_name, max_elements_per_file=10000):
    """
    Save a list of objects to multiple JSON files, each containing a maximum number of elements.

    Args:
        data (list): The list of objects to save.
        output_file_prefix (str): Prefix for the output JSON file names.
        max_elements_per_file (int): Maximum number of elements per JSON file.
    """
    
    # Ensure the folder exists
    os.makedirs(folder_name, exist_ok=True)
    
    file_count = 0
    # Split the list into chunks of max_elements_per_file
    for i in range(0, len(data), max_elements_per_file):
        file_count += 1
        chunk = data[i:i + max_elements_per_file]
        file_name = f"{output_file_prefix}_{file_count}.json"
        # Create the full file path
        file_path = os.path.join(folder_name, file_name)
        with open(file_path, "w") as json_file:
            json.dump(chunk, json_file, ensure_ascii=False)
        print(f"Saved {len(chunk)} elements to {file_name}")
