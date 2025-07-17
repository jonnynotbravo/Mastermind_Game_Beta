import requests 
import random

def secret_code():
    try: 
        url = 'https://www.random.org/integers/'
        # Make params incase modification is needed
        params = {
            'num': 4,
            'min': 0,
            'max': 7,
            'col': 1,
            'base': 10,
            'format': 'plain',
            'rnd': 'new'
        }

        # Response data of the URL
        response = requests.get(url, params=params, timeout=5)
        response.raise_for_status()
        # Ensures the type of data fetched
        # return (response.headers["Content-Type"])
        data = response.text
        # Remove any whitespace and split it
        str_arr = data.strip().splitlines()
        secret_code = [int(x) for x in str_arr]
        return secret_code
    
    except (
        requests.exceptions.Timeout,
        requests.exceptions.ConnectionError,
        requests.exceptions.HTTPError,
        requests.exceptions.RequestException,
        ValueError, IndexError, KeyError
    ):
        
        # Fallback Random Number generator incase API fails
        secret_code = [random.randint(0,7) for _ in range(4)]
        return secret_code
