from openai import OpenAI

def get_completion(client, prompt, model="gpt-3.5-turbo", temperature = 0) -> str:
    messages = [{"role": "user", "content": prompt}]
    response = client.chat.completions.create(
        model=model, # "gpt-3.5-turbo"  or "gpt-4"
        messages=messages,
        temperature=temperature,
        response_format={ "type": "json_object" },
    )
    return response.choices[0].message.content