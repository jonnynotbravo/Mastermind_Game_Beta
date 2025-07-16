# Mastermind_Game_Beta

import requests

def generate_secret_code(): 

    try:
        url = 'https://www.random.org/integers/'
        params = {
            'num': 4,
            'min': 0,
            'max': 7,
            'col': 1,
            'base': 10,
            'format': 'plain',
            'rnd': 'new'
        }

        response = requests.get(url, params=params, timeout=5)
        response.raise_for_status()
        data = response.text
        string = data.strip().splitlines()
        return lines


        # secret_code = [int(x) for x in lines]
        # return secret_code
    
    except (
        requests.exceptions.Timeout,
        requests.exceptions.ConnectionError,
        requests.exceptions.HTTPError,
        requests.exceptions.RequestException,
        ValueError, IndexError, KeyError):
    
        return 'Error Generating Secret code from Random.org'



print(generate_secret_code())