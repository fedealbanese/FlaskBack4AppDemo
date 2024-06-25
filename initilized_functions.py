import json 
from os import listdir

def initilized_templates(examples_path: str):
    """
    Initializes templates and response dictionaries from JSON files in the specified directory.

    Parameters:
    - examples_path (str): Path to the directory containing JSON files.

    Returns:
    - tuple: A tuple containing two dictionaries:
        - templates (dict): Keys are API names (from JSON file names), values are template strings.
        - response_dicts (dict): Keys are API names, values are JSON content from the files.
   """
    templates = {}
    response_dicts = {}
    json_files = [f for f in listdir(examples_path) if f.endswith(".json")]
    for file_name in json_files:
        api_name = file_name[:-5] #without .json
        with open(examples_path+file_name) as f:
            response_dict = json.load(f)
        template = f"{{{{ '{api_name}' : {{{api_name}}} }}}}"
        templates[api_name] = template
        response_dicts[api_name] = response_dict
    return templates, response_dicts

def initiate_state(examples_path:str):
    """
    Initializes user state from JSON files in the specified directory.

    Parameters:
    - examples_path (str): Path to the directory containing JSON files.

    Returns:
    - user_state (dict): Keys are API names (from JSON file names), values are template strings.
   """
    user_state = {}
    json_files = [f for f in listdir(examples_path) if f.endswith(".json")]
    for file_name in json_files:
        api_name = file_name[:-5] #without .json
        with open(examples_path+file_name) as f:
            response_dict = json.load(f)
        user_state[api_name] = response_dict
    return user_state
