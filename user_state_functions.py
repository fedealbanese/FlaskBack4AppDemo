import ast
import json
from openAI_functions import get_completion

def update_state_from_configuration(OpenAI_client, user_state, input_configuration):
    prompt = f"""
        Este es un usuario bancario descripto en formato json:
        
        {user_state}

        Modifica las keys y/o values del json a partir de las siguientes consideraciones:
        {input_configuration}
        
        Respeta y mantene el formato, largo y tipo de los valores.
        El nuevo json:
        """
    response = get_completion(OpenAI_client, prompt)
    print("New configuration:", input_configuration)
    print("GPT response:", response)
    new_user_state = ast.literal_eval(response.replace('null', 'None').replace("true","True").replace("false","False").replace("\t"," ").replace("\n"," "))
    return  new_user_state

def update_state_from_api(OpenAI_client, user_state, api_request): #TODO
    #xclient_state["saldo"] = int(client_state["saldo"]) - int(re.search(r'<importe>(.*?)</importe', api_request).group(1) )
    prompt = f"""
    Se te proporciona un objeto JSON que representa el estado de un usuario de banco y una solicitud de API. Tu tarea es modificar el objeto JSON según la solicitud de API. Por ejemplo, si la solicitud de API es una transferencia bancaria, debes reducir el saldo de la cuenta bancaria del usuario por el monto de la transferencia. Asegúrate de validar la solicitud y manejar los errores apropiadamente, como fondos insuficientes para una transferencia bancaria. Devuelve el objeto JSON modificado.
    Aquí está el objeto JSON y la solicitud de API:
    Estado del Usuario del Banco (JSON):
    
    {user_state}

    Solicitud de API:
    {api_request}
    Respeta y mantene el formato, largo y tipo de los valores.
    Por favor, modifica el objeto JSON según la solicitud de API y proporciona el JSON actualizado.
    """
    response = get_completion(OpenAI_client, prompt)
    new_user_state = ast.literal_eval(response.replace('null', 'None').replace("true","True").replace("false","False").replace("\t"," ").replace("\n"," "))
    print("Modifing the state based on api request.")
    print("GPT response:", response)
    print("new_client_state", new_user_state)
    return new_user_state