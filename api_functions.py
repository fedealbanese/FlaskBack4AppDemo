from flask import make_response, jsonify

def generate_response(api_endpoint: str, user_state: dict, response_dicts: dict):
    """
    Generates a response by merging user state with default response data.

    Parameters:
    - api_endpoint (str): The API endpoint name.
    - user_state (dict): The user's current state data.
    - response_dicts (dict): The default response data for all endpoints.

    Returns:
    - Response: A Flask response object containing the merged JSON data.
    """
    if type(response_dicts[api_endpoint]) == dict:
        response_dict = {}
        for key in response_dicts[api_endpoint]:
            if key in user_state[api_endpoint]:
                response_dict[key] = user_state[api_endpoint][key]
            else:
                response_dict[key] = response_dicts[api_endpoint][key]
        jsonify_account_summery = jsonify(response_dict)
        response = make_response(jsonify_account_summery)
        print(jsonify_account_summery)
        print(response_dict) #print(json.dumps(account_summery, indent=2))
        return response
    else: #is a list:
        response_dict = user_state[api_endpoint]
        jsonify_account_summery = jsonify(response_dict)
        response = make_response(jsonify_account_summery)
        print(jsonify_account_summery)
        print(response_dict) #print(json.dumps(account_summery, indent=2))
        return response