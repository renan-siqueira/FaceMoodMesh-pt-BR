import json


def load_json(filepath):
    """
    Carrega um arquivo JSON e retorna seu conteúdo.

    Parâmetros:
    - filepath (str): O caminho para o arquivo JSON que deve ser lido.

    Retorna:
    - dict: O conteúdo do arquivo JSON como um dicionário.
    """
    
    with open(filepath, 'r', encoding='utf-8') as file:
        messages = json.load(file)
    return messages
